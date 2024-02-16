import os
import subprocess

from django_cron import CronJobBase, Schedule
from dotenv import load_dotenv

load_dotenv()


class UpdateRate(CronJobBase):

    RUN_EVERY_MINS = 1
    MAILTO = os.getenv("EMAIL")

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "update_rate"

    def do(self):
        cmd = ["python", "currency_rate/manage.py", "update_currency_rate"]
        subprocess.run(cmd)
