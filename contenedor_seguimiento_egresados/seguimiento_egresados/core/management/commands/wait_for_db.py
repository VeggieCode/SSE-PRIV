import time

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from pymysql import OperationalError as PyMySQLError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        is_db_up = False
        while is_db_up is False:
            try:
                self.check(databases=['default'])
                is_db_up = True
            except (PyMySQLError, OperationalError):
                self.stdout.write('Database unavailable waiting 5 second.')
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS('Database up!'))
