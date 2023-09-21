import os

from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

print(DATABASE_URL)
os.system(f'prisma db push --schema .\\prisma\\chinook.prisma')


def insert_file(file_name):
    print(f'prisma db execute --file .\\prisma\\{file_name}.sql --url {DATABASE_URL}')
    os.system(f'prisma db execute --file .\\prisma\\{file_name}.sql --url {DATABASE_URL}')


insert_file('artists')
insert_file('albums')
insert_file('employees')
insert_file('customers')
insert_file('genres')
insert_file('media_types')
insert_file('tracks')
insert_file('playlists')
insert_file('playlist_track')
insert_file('invoices')
insert_file('invoice_items')
