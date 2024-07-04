from fastapi import FastAPI

def create_app():
    return FastAPI(
        title='Simple Kafka Chat',
        docs_url='/api/docs',
        description='Simple Kafka + ddd.',
        debug=True,
    )
