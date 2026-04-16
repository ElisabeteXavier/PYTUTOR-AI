from fastapi import FastAPI


from back.routes import routes

app = FastAPI()


app.include_router(routes)