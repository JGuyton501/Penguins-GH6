import csv
import datetime
from dateutil.parser import parse
from value_maps import ethnicity, war_participated
from api.models import Client
from api.models import Services

def sync_client():
    with open('sample_data/client.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        ethnicity_funct = lambda k: [name for name in ethnicity.keys() if int(k[name])]
        war_participated_funct = lambda k: [war_participated[name] for name in war_participated.keys() if int(k[name])]
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

                csv2db_client = {
                    "uuid": row["UUID"],
                    "first_name": row["First_Name"],
                    "middle_name": row["Middle_Name"],
                    "last_name": row["Last_Name"],
                    "social_security": row["SSN"],
                    "date_of_birth": fmt_date(row["DOB"]),
                    "gender": int(row["Gender"]) if row['Gender'] else None,
                    "veteran": int(row["VeteranStatus"]) if row['VeteranStatus'] else None,
                    "year_entered": int(row["YearEnteredService"]) if row['YearEnteredService'] else None,
                    "year_exited": int(row["YearSeparated"]) if row['YearSeparated'] else None,
                    "military_branch": int(row["MilitaryBranch"]) if row['MilitaryBranch'] else None,
                    "discharge_status": row["Discharge_Status"],
                    "date_created": fmt_datetime(row["Date_Created"]),
                    "date_updated": fmt_datetime(row["DateUpdated"]),
                    "associate_id": row["UserID"],
                    "ethnicity": ethnicity[ethnicity_funct(row)[0]],
                    "war_participated": war_participated_funct(row)
                }

            bulk_create.append(Client(**csv2db_client))
        import pdb; pdb.set_trace()


def sync_services():
    with open('sample_data/services.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []
        #Format functions where applicable
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

                csv2db_client = {
                    "personal_id" : row["PersonalID"],
                    "project_entry_id" : row["ProjectEntryID"],
                    "services_id" : row["ServicesID"],
                    "date_provided" : fmt_date(row["DateProvided"]),
                    "record_type" : int(row["RecordType"]) if row['RecordType'] else None,
                    "type_provided" : int(row["TypeProvided"]) if row['TypeProvided'] else None,
                    "other_type_provided" : int(row["OtherTypeProvided"]) if row['OtherTypeProvided'] else None,
                    "sub_type_provided" = int(row["SubTypeProvided"]) if row['SubTypeProvided'] else None,
                    "fa_amount" : int(row["FAAmount"]) if row['FAAmount'] else None,
                    "referral_outcome" = row["ReferralOutcome"],
                    "date_created" : fmt_datetime(row["DateCreated"]),
                    "date_updated" : fmt_datetime(row["DateUpdated"]),
                    "associate_id" : row["UserID"]
                }

                bulk_create.append(Client(**csv2db_client))
  
