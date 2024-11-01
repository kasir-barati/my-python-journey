# PyMongo

-   Python binding for the MongoDB
-   `pip3 install pymongo`
-   I'm gonna use dockerized MongoDB. The rc version.
    -   **RC** means that you won't get unpredictable notice to update your MongoDB image. This is my observation from [this GitHub issue](https://github.com/linuxserver/docker-jellyfin/issues/79).
    -   Here is a short about what I did:
        -   I said to create a volume for me. The name would be `sixth_lama_mongodb_volume`
        -   You can change the username and password through `.mongodb.env`. I added an example env file.
        -   It will bind 27018 to 27017
