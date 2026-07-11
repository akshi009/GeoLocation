from fastapi import FastAPI,Request
import requests

app=FastAPI()

@app.get('/track')
async def getInfo(request:Request):
    ip = request.headers.get("x-forwarded-for", request.client.host)

    geo = requests.get(f"http://ip-api.com/json/{ip}").json()

    print("ip ->", ip)
    print("city ->", geo.get("city"))
    print("region ->", geo.get("regionName"))
    print("country ->", geo.get("country"))
    print("lat/lon ->", geo.get("lat"), geo.get("lon"))

    return {"status":"OK"}

