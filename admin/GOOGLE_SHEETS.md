
## Google Sheets Database Setup

Ensure you have followed the [Google Cloud Setup](/admin/GOOGLE_CLOUD.md) guide, specifically that you have enabled the "Google Sheets API", and have downloaded the service account JSON file into the root directory of this repository and renamed it as "google-credentials.json".

#### Document Setup

Create a new Google Sheet document. The app will need read and write access to this document.

Modify the document's sharing settings to grant "Edit" privileges to the "client email" address specified in the Google API credentials JSON file (e.g. "`<my-serice>`@`<my-project>`.iam.gserviceaccount.com").

#### Sheets Setup

Create two example sheets. One called "products" and the other called "orders".

On the "products" sheet, populate the first row with the following column headers:

  + `id`
  + `name`
  + `description`
  + `price`
  + `url`
  + `created_at`

On the "orders" sheet, populate the first row with the following column headers:

  + `id`
  + `product_id`
  + `user_email`
  + `created_at`

You will notice there are corresponding "model" classes defined in the "app/models" directory. For any sheet, the fields defined in the corresponding model class need to stay consistent with the column names designated in the sheet.


For any new sheet that you would like to create, you will need to repeat and adapt this process, including defining a new model class, and importing it in the "________" file.



### WIP


**Seeding the Database**

Seed the database to automatically populate it with example product records:


```sh
python -m app.sheets_service
```

name | description | price | url
--- | --- | --- | ---
Strawberries | Juicy organic strawberries. | 4.99 | https://picsum.photos/id/1080/360/200
Cup of Tea | An individually-prepared tea or coffee of choice. | 3.49 | https://picsum.photos/id/225/360/200
Textbook | It has all the answers. | 129.99 | https://picsum.photos/id/24/360/200
