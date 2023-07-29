"""
Wait for database to start
"""
import time

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Pyscopg2OpError

class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting fro database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pyscopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting for 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

