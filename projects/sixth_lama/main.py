from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection


def main() -> None:
    client = MongoClient("localhost", 27018)
    db = client.learning
    videos = db.videos

    videos_count = videos.count_documents({});
    print(f"videos_count: {videos_count}")
    
    fetched_videos = videos.find({})
    print("fetched_videos: ", )
    for index in range(0, videos_count):
        temp = fetched_videos.next()

        if temp == None:
            break
        print(f"{index}: {temp}")
    
    videos_contains_sql = videos.find({"name": { "$regex": "sql" }})
    print("videos_contains_sql: ")
    for i in range(0, videos_count):
        temp = videos_contains_sql.retrieved

        if temp == None:
            break
        print(temp)


def insert_data(videos: Collection) -> None:
    video = {"name": "SQLDB"}
    list_of_videos = [{"name": "MonPostDB"}]
    inserted_video = videos.insert_one(video);
    inserted_videos = videos.insert_many(list_of_videos);
    print(f"inserted_video.inserted_id: {inserted_video.inserted_id}")
    print(f"inserted_videos.inserted_ids: {inserted_videos.inserted_ids}")


main()

