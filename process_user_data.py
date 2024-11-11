import os
import sys
import json
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Procesar datos de usuario de Garmin.')
    parser.add_argument('--config', help='Ruta al archivo GarminConnectConfig.json', required=True)
    args = parser.parse_args()

    config_path = args.config

    # Cargar el archivo GarminConnectConfig.json
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Extraer el correo electrónico del usuario
    email = config['credentials']['user']
    if not email:
        print('Correo electrónico no encontrado en la configuración.')
        sys.exit(1)

    # Crear una carpeta basada en la dirección de correo electrónico
    # Reemplazar '@' y '.' en el correo para crear un nombre de carpeta válido
    safe_email = email.replace('@', '_at_').replace('.', '_')
    user_folder = os.path.join(os.getcwd(), safe_email)
    os.makedirs(user_folder, exist_ok=True)

    print(f'Carpeta de usuario creada: {user_folder}')

    # Actualizar la configuración para usar la carpeta específica del usuario
    # Por ejemplo, actualizar 'directories' -> 'base_dir' para que apunte a la carpeta del usuario
    config['directories']['base_dir'] = user_folder

    # Guardar la configuración actualizada en la carpeta del usuario
    user_config_path = os.path.join(user_folder, 'GarminConnectConfig.json')
    with open(user_config_path, 'w') as f:
        json.dump(config, f, indent=4)

    print(f'Configuración actualizada guardada en: {user_config_path}')

    # Ejecutar el script de GarminDB con la configuración actualizada
    # Asumiendo que garmindb_cli.py está en la carpeta GarminDB-master/scripts
    script_dir = os.path.dirname(os.path.abspath(__file__))
    garmin_db_script = os.path.join(script_dir, 'GarminDB-master', 'scripts', 'garmindb_cli.py')

    if not os.path.isfile(garmin_db_script):
        print(f'Script de GarminDB no encontrado en {garmin_db_script}')
        sys.exit(1)

    # Construir el comando para ejecutar el script de GarminDB
    command = [
        sys.executable,  # Usa el mismo intérprete de Python
        garmin_db_script,
        '--all',
        '--download',
        '--import',
        '--analyze',
        '--latest',
        '--config', user_config_path
    ]

    print('Ejecutando script de GarminDB...')
    result = subprocess.run(command)

    if result.returncode != 0:
        print('El script de GarminDB falló.')
        sys.exit(result.returncode)

    print('Procesamiento de datos del usuario completado.')

if __name__ == '__main__':
    main()
