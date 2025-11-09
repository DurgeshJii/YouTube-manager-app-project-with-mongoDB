#***************************YouTube Manager Project Using Mongo_DB**********************************
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://justdevil2003_db_user:d6zbWaE7FhvILCZG@cluster0.g7dgec4.mongodb.net/",
    tlsAllowInvalidCertificates=True
)
db = client["ytmanager"]
video_collection = db["videos"]

def list_videos():
    videos = list(video_collection.find())
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")

def add_video(name, time):
    try:
        video_collection.insert_one({"name": name, "time": time})
        print("✅ Video added successfully!")
    except Exception as e:
        print("❌ Error:", e)

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {"name": new_name, "time": new_time}}
    )
    print("✅ Video updated successfully!")

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    print("✅ Video deleted successfully!")

def main():
    while True:
        print("\n🎬 YouTube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting YouTube Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
