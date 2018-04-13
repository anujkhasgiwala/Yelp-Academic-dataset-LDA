import json
import csv

file_data = []
def readFile():
    with open("yelp_dataset_challenge_round9\yelp_academic_dataset_business.json", 'r', encoding='utf8') as input_file:
        for line in input_file:
            file_data.append(json.loads(line))

def toCSV(file_data):
    with open('yelp_business2.csv', 'a', newline='') as business_id:
        csvwriter = csv.writer(business_id)
        for data in file_data:
            if data['city'] == "Pittsburgh" or data['city'] == "Charlotte":
                csvwriter.writerow((data['city'], data['business_id'], data['categories']))

def toCSVChinese(file_data):
    with open('yelp_business2.csv', 'a', newline='') as business_id:
        csvwriter = csv.writer(business_id)
        for data in file_data:
            if data['city'] == "Pittsburgh" or data['city'] == "Charlotte":
                try:
                    if (data['categories'] is not None) and ("Chinese" in data['categories']):
                        csvwriter.writerow((data['city'], data['business_id'], data['categories']))
                except:
                    pass

def categories():
    count=0
    with open('yelp_business1.csv', 'r') as business_id1_file:
        file1_read = csv.reader(business_id1_file)
        for line1 in file1_read:
            city = line1[0]
            line1 = line1[2]
            line1 = line1.replace("[", "")
            line1 = line1.replace("]", "")
            line1 = line1.replace("\'", "")
            temp = line1.split(',')
            for elem in temp:
                count += 1
                elem = elem.strip()
                with open('category.csv', 'a', newline='') as category:
                    csvwriter = csv.writer(category)

#get checkin and review details and save them in csv
checkin_data = []
review_data=[]

def getcheckin():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    with open('yelp_business.csv', 'r') as business_id_file:
        file_read = csv.reader(business_id_file, delimiter=',')
        for line in file_read:
            with open("yelp_dataset_challenge_round9\yelp_academic_dataset_checkin.json", 'r', encoding='utf8') as checkin_file:
                for checkin in checkin_file:
                    checkin_data.append(json.loads(checkin))
                for check in checkin_data:
                    if check['business_id'] == line[1]:
                        with open('yelp_checkin.csv', 'a', newline='') as checkins:
                            csvwriter = csv.writer(checkins)
                            csvwriter.writerow((check['time'],check['business_id'],check['type']))

def getReview():
    global review_file1
    with open('yelp_business.csv', 'r') as business_id_file:
        file_read = csv.reader(business_id_file, delimiter=',')
        for line in file_read:
            with open("/home/vikas/Desktop/New folder/yelp_dataset_challenge_round9/yelp_academic_dataset_review.json", 'r',encoding='utf8') as review_file1:
                for reviews in review_file1:
                    review_data.append(json.loads(reviews))
                for review in review_data:
                    if review['business_id'] == line[1]:
                        with open('yelp_review.csv', 'a') as reviews:
                            csvwriter = csv.writer(reviews)
                            csvwriter.writerow((review['review_id'], review['user_id'], review['business_id'],
                                                    review['stars'], review['date'], review['text'], review['useful'],
                                                    review['funny'], review['cool'], review['type']))

def getReviewChinese():
    global review_file1
    with open('yelp_business2.csv', 'r') as business_id_file:
        file_read = csv.reader(business_id_file, delimiter=',')
        for line in file_read:
            with open("/home/vikas/Desktop/New folder/yelp_dataset_challenge_round9/yelp_academic_dataset_review.json", 'r',encoding='utf8') as review_file1:
                for reviews in review_file1:
                    review_data.append(json.loads(reviews))
                for review in review_data:
                    if review['business_id'] == line[1]:
                        with open('yelp_review1.txt', 'a') as reviews:
                            csvwriter = csv.writer(reviews)
                            csvwriter.writerow(("Anuj", review['text']))

#readFile()
#toCSVChinese(file_data)
#categories()
#getcheckin()
#getReview()
getReviewChinese()