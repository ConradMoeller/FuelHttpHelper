import configparser
import os
import time

import requests

if __name__ == '__main__':
    config = configparser.ConfigParser()

    config['FuelHttpHelper'] = {
        'domain': 'synergy-sgkp-example.test-cloud.bi-web.de',
        'user': 'nutzername',
        'password': 'passwort',
        'interval': '0',
        'delete': 'True',
        'channels': "lastgang-csv|lastgang-mscons|lastgang-xml|stammdaten-csv"
    }

    if not os.path.isfile('FuelHttpHelper.ini'):
        with open('FuelHttpHelper.ini', 'w') as configfile:
            print("Neue Konfigurationsdatei erstellt.")
            config.write(configfile)
    else:
        config.read('FuelHttpHelper.ini')

    # Infinite loop unless exit is called
    while True:
        try:
            # Get the domain, user and password from the config file
            domain = config['FuelHttpHelper']['domain']
            if not domain or domain == 'synergy-sgkp-example.test-cloud.bi-web.de' or \
                    'http' in domain or 'services.' in domain or '/' in domain:
                print(
                    'Bitte tragen Sie die Domain Ihres Portals bis zum ersten "/" ohne ' +
                    '"http(s)://" oder "services." in die FuelHttpHelper.ini ein.')
                time.sleep(10)
                exit(1)

            user = config['FuelHttpHelper']['user']
            password = config['FuelHttpHelper']['password']

            if not user or not password or user == 'nutzername' or password == 'passwort':
                print('Bitte tragen Sie Nutzername und Passwort in FuelHttpHelper.ini ein.')
                time.sleep(10)
                exit(1)

            fuel_http_server = 'https://services.' + domain + '/portal/servlet/com.busintel.fuel.http.FuelHTTPServer'
            folders_to_check = config['FuelHttpHelper']['channels'].split('|')
            delete = config['FuelHttpHelper']['delete'].lower() == 'true'

            number_of_files = 0

            for folder in folders_to_check:
                if not os.path.exists(folder):
                    os.makedirs(folder)
                for file in [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]:

                    with open(os.path.join(folder, file), "r") as file_content:
                        payload = {
                            'message': (None, file_content),
                            'filename': (None, file),
                            'filesize': (None, file_content),
                            'channel': (None, folder)
                        }

                        response = requests.post(fuel_http_server, files=payload, auth=(user, password))

                    print("Kanal: " + folder + ", Datei: " + file + ", Statuscode:", response.status_code)

                    if delete:
                        os.remove(os.path.join(folder, file))
                        print(folder + "/" + file + " gelöscht!")

                    number_of_files += 1

            if not number_of_files:
                print("Keine Dateien zum Hochladen gefunden.")
                time.sleep(10)
            else:
                print("Hochgeladene Dateien: " + str(number_of_files))
                time.sleep(10)

            interval = int(config['FuelHttpHelper']['interval'])
            if interval:
                print("Wartezeit bis zum nächsten Lauf in Minuten: " + str(interval))
                time.sleep(interval * 60)  # Sleep for the given interval in minutes
            else:
                exit(0)

        except Exception as e:
            print("Es ist ein Fehler aufgetreten: " + str(e))
            exit(1)
