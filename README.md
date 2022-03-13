# InterviewAdminPortal

git clone

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

- Get List of Interviews

curl --location --request GET 'https://intellisenseviz.herokuapp.com/interviews/' \
--header 'Content-Type: application/json' \
--data-raw ''

- Update Interview

curl --location --request PUT 'https://intellisenseviz.herokuapp.com/interviews/bf538efc-036e-4c4f-ae7f-7dabdb2d669b/' \
--header 'Content-Type: application/json' \
--data-raw ' {
        "interviewer": [
            {
                "id": 1,
                "examiner": {
                    "username": "17shashank17",
                    "email": "17shash@gmail.com",
                    "is_staff": true
                },
                "contact": "+91 xxxxxxxxxx",
                "experience": 2
            },
            {
                "id": 2,
                "examiner": {
                    "username": "shivani",
                    "email": "",
                    "is_staff": false
                },
                "contact": "+91 xxxxxxxxxx",
                "experience": 2
            }
        ],
        "participants": [
            {
                "id": 11,
                "student": {
                    "username": "shraddha",
                    "email": "",
                    "is_staff": false
                },
                "contact": "+91 xxxxxxxxxx",
                "badge": 1
            }
        ],
        "organization": "Confluence & Conf",
        "name": "Default Competetion",
        "difficulty": "Easy",
        "isPublic": true,
        "startTime": "1647169736000",
        "endTime": "1647175751000",
        "update_at": "1647169736000",
        "description": "Kaggle AI contest for automatic question generation"
    }'

Note: pls dont change interviewer and participants while updating


- Add participants

curl --location --request POST 'https://intellisenseviz.herokuapp.com/addParticipants/' \
--header 'Content-Type: application/json' \
--data-raw '    {
        "competitionId": "bf538efc-036e-4c4f-ae7f-7dabdb2d669b",
        "participants": ["shraddha"]
    }'

- Add interviewers

curl --location --request POST 'https://intellisenseviz.herokuapp.com/addInterviewer/' \
--header 'Content-Type: application/json' \
--data-raw '    {
        "competitionId": "bf538efc-036e-4c4f-ae7f-7dabdb2d669b",
        "interviewers": ["17shashank17", "shivani"]
    }'

- Check If slot is available

curl --location --request POST 'https://intellisenseviz.herokuapp.com/checkSlot/' \

--header 'Content-Type: application/json' \
--data-raw '    {
        "username": "shraddha",
        "slot_start_ts": "1647169737000",
        "slot_end_ts": "1647169738000"
    }'
