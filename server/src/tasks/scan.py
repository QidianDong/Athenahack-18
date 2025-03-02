from launcher import celery


@celery.task(name="scan.add")
def add(x, y):
    return x + y
