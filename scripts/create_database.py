import os

from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

print(DATABASE_URL)
os.system('prisma db push --schema .\\prisma\\chinook.prisma')


def execute_file(file_name):
    print(f'prisma db execute --file .\\prisma\\{file_name}.sql --url {DATABASE_URL}')
    os.system(f'prisma db execute --file .\\prisma\\{file_name}.sql --url {DATABASE_URL}')


execute_file('truncate')
execute_file('artists')
execute_file('albums')
execute_file('employees')
execute_file('customers')
execute_file('genres')
execute_file('media_types')
execute_file('tracks')
execute_file('playlists')
execute_file('playlist_track')
execute_file('invoices')
execute_file('invoice_items')
execute_file('sequences')
