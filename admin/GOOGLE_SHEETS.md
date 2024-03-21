## Google Sheets API Setup

From the Google APIs project console, enable the Google Sheets APIs.
![alt text](/.github/markdown-images/admin/image-1.png)
![alt text](/.github/markdown-images/admin/image.png)

Ensure the Google API Credentials file for this project is stored locally as "google-credentials.json" (from previous README step).

### Google Sheets Database Setup

Create a new Google Sheet document.

![alt text](/.github/markdown-images/admin/image-2.png)

Modify the document's sharing settings to grant "edit" privileges to the Service Account email address specified in the Google API credentials file (shown above).

**Products Sheet**

Create a new sheet called "products", and add an initial row of column headers:

- `id`
- `name`
- `description`
- `price`
- `url`
- `created_at`

**Orders Sheet**

Create a new sheet called "orders", and add an initial row of column headers:

- `id`
- `product_id`
- `user_email`
- `created_at`

You'll need the document ID for your python .env file, which can be found in the URL (the string between /d/ and /edit)

![alt text](/.github/markdown-images/admin/image-3.png)

**Seeding the Database**

After configuring your Python .env file, seed the database to automatically populate it with example product records:

```sh
python -m app.spreadsheet_service
```

| name         | description                                       | price  | url                                   |
| ------------ | ------------------------------------------------- | ------ | ------------------------------------- |
| Strawberries | Juicy organic strawberries.                       | 4.99   | https://picsum.photos/id/1080/360/200 |
| Cup of Tea   | An individually-prepared tea or coffee of choice. | 3.49   | https://picsum.photos/id/225/360/200  |
| Textbook     | It has all the answers.                           | 129.99 | https://picsum.photos/id/24/360/200   |
