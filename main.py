import asyncio
from contextlib import asynccontextmanager
from datetime import datetime

from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI

from apscheduler.schedulers.background import BackgroundScheduler

from check_product import check_little_sleepies, check_meyers


# Define your scheduled tasks
async def minute_task():
    print(f"Running minute task at {datetime.now()}")
    check_little_sleepies("around-the-world-large-cloud-blanket", "")
    check_meyers("bourbon-red-heritage-day-old-turkey-poults")
    check_meyers("narragansett-heritage-day-old-turkey-poults")
    check_meyers("black-spanish-heritage-day-old-turkey-poults")
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
        trigger=CronTrigger(minute='*/5'),  # Run every hour
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



