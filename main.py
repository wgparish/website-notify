import asyncio
from contextlib import asynccontextmanager
from datetime import datetime

from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI

from apscheduler.schedulers.background import BackgroundScheduler

from check_product import check_little_sleepies, check_newegg
from config import SEND_SMS_TO_GPU


# Define your scheduled tasks
async def minute_task():
    print(f"Running minute task at {datetime.now()}")
    check_newegg("acer-nitro-an-b580-oca-intel-12gb-gddr6/p/N82E16814553012", SEND_SMS_TO_GPU)
    check_newegg("p/N82E16814883006", SEND_SMS_TO_GPU)
    # Your task logic here

# Wrapper function to handle async tasks
def run_async_task(task):
    asyncio.run(task())

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the scheduler
    scheduler.start()

    # Add jobs to the scheduler
    scheduler.add_job(
        run_async_task,
        trigger=CronTrigger(second='*/15'),
        id='minute_task',
        name='Run minute task',
        args=[minute_task],
        misfire_grace_time=None
    )

    print("Scheduled tasks started")
    yield
    # Shutdown scheduler on app shutdown
    scheduler.shutdown()
    print("Scheduled tasks stopped")

app = FastAPI(lifespan=lifespan)

# Create scheduler
scheduler = BackgroundScheduler()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/check-stock/{product_id}")
async def product_check(product_id: str):
    check_little_sleepies(product_id, "")



