#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:50:55 2020

@author: safir
"""

import random
import copy

class DataGenerator:
    def __init__(self):
        
        # House Data Initialization

        self.house_struct = ['Bungalow', 'Building', 'Row House']
        self.house_type = ['Furnished House', 'Unfurnished House']
        
        
        self.building = ['https://res.cloudinary.com/safcloud/image/upload/v1606385427/TenouseDataGen/Building/daniel-dinuzzo-qCjolcMFaLI-unsplash_jceqni.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385427/TenouseDataGen/Building/SmartBuilding_iygbxj.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385426/TenouseDataGen/Building/f5bcc8800cce5935bf4e7b7d73860882_tcqd9z.jpg' 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385426/TenouseDataGen/Building/Building_Wish-Town-696x392_tulu6m.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385426/TenouseDataGen/Building/unnamed_caziu2.jpg']
        
        self.bungalow = ['https://res.cloudinary.com/safcloud/image/upload/v1606385872/TenouseDataGen/Bungalow/the-110-year-old-california-craftsman-bungalow-is-at-once-rich-in-history-and-entirely-suited-to-todays-discerning-tastes_leutjm.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385872/TenouseDataGen/Bungalow/stringio_dvuzbl.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606385871/TenouseDataGen/Bungalow/1-storey-house-12_leeqdz.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606384529/TenouseDataGen/Bungalow/florian-schmidinger-b_79nOqf95I-unsplash_nycnbl.jpg', 
                    'https://res.cloudinary.com/safcloud/image/upload/v1606384529/TenouseDataGen/Bungalow/naomi-ellsworth-EMPLSuvDuhQ-unsplash_cvksnx.jpg']
        
        self.row_house = ['https://res.cloudinary.com/safcloud/image/upload/v1606386041/TenouseDataGen/Row%20House/row-of-houses-1_hxesfz.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386040/TenouseDataGen/Row%20House/thebungalows_mainbanner2_is5fyr.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386039/TenouseDataGen/Row%20House/unnamed_nxkojq.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386038/TenouseDataGen/Row%20House/921f10825343bdd1f375f7ae5c6897f9_dai7pv.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606384560/TenouseDataGen/Row%20House/digital-marketing-agency-ntwrk-g39p1kDjvSY-unsplash_b8qv4h.jpg']
        
        self.furnished = ['https://res.cloudinary.com/safcloud/image/upload/v1606386917/TenouseDataGen/Furnished/selling-furnished-home_fohp0r.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386917/TenouseDataGen/Furnished/slider02_opktfg.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386917/TenouseDataGen/Furnished/unnamed_st4efr.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386917/TenouseDataGen/Furnished/home-design_jmttuv.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606386917/TenouseDataGen/Furnished/Semi-furnished-furnished-fully-furnished-apartment-How-are-they-different-FB-1200x700-compressed-686x400_ki7zwe.jpg']
        
        self.unfurnished_house = ['https://res.cloudinary.com/safcloud/image/upload/v1606386934/TenouseDataGen/Unfurnished/unfurnished-old-lane-house-on-dingxi-rd-with-private-garden-and-terrace-800_533-28050_dfgjf3.jpg', 
                             'https://res.cloudinary.com/safcloud/image/upload/v1606386934/TenouseDataGen/Unfurnished/44587648027e8d34fdec041b56f2cad8cec87cbc_l2uciv.jpg', 
                             'https://res.cloudinary.com/safcloud/image/upload/v1606386933/TenouseDataGen/Unfurnished/four-bedroom-house-for-sale-near-CMU-7-of-10_rjiyvf.jpg', 
                             'https://res.cloudinary.com/safcloud/image/upload/v1606386933/TenouseDataGen/Unfurnished/unfurnished-living-room-interior-old-craftsman-house-gray-walls-hardwood-floors-fireplace-northwest-usa-79896885_gl9bir.jpg', 
                             'https://res.cloudinary.com/safcloud/image/upload/v1606386933/TenouseDataGen/Unfurnished/house-for-rent-ID-H140-7_qoyqop.jpg']
        
        self.house_struct_obj = {
            'Bungalow':self.bungalow,
            'Building':self.building,
            'Row House':self.row_house
            }
        
        self.house_type_obj = {
            'Furnished House':self.furnished,
            'Unfurnished House':self.unfurnished_house
            }
        
        self.house_question1 = ['18-25', '26-30', '31-45', '46-60', 'Cool with any']
        self.house_question2 = ['Married', 'Not Married']
        self.house_question3 = ['2500', '5000', '7500', '10000']
        self.house_question4 = ['This is a wonderful house at a scenic view', 'This is a beutiful house in the city area',
                     'This is an amazing house in a serene place', "This is the house that you'd want to stay", 
                     'This is a sweet little palace']
        self.house_question5 = ['Salunke Vihar Road', 'NIBM', 'Azad Nagar', 'Koregaon Park']
        self.house_question6 = ['Pune', 'Mumbai', 'Bangalore', 'Hyderabad']
        self.house_question7 = {'Pune':'Maharashtra', 'Mumbai':'Maharashtra', 'Bangalore':'Karnataka', 'Hyderabad':'Telangana'}
        self.house_question8 = ['India']
        self.house_question9 = {'Pune':'411022', 'Mumbai':'230532', 'Bangalore':'530068', 'Hyderabad':'500001'}
        
        
        # Roommate Data Initialization
        
        self.male = ['https://res.cloudinary.com/safcloud/image/upload/v1606389491/TenouseDataGen/Male/seth-doyle-Vnm4aweBwPA-unsplash_ixkdb1.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606389488/TenouseDataGen/Male/utopia-MS0RHQ1enek-unsplash_sydspp.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606389487/TenouseDataGen/Male/midas-hofstra-tidSLv-UaNs-unsplash_fqqndr.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606389487/TenouseDataGen/Male/seth-doyle-vmBik4xv27s-unsplash_tb13js.jpg', 
                     'https://res.cloudinary.com/safcloud/image/upload/v1606389486/TenouseDataGen/Male/keenan-lynch-jGlYxKAJ9cc-unsplash_tpnoez.jpg']
        
        self.female = ['https://res.cloudinary.com/safcloud/image/upload/v1606389507/TenouseDataGen/Female/raychan-9UkAHVs5y7Y-unsplash_qniqoc.jpg', 
                       'https://res.cloudinary.com/safcloud/image/upload/v1606389507/TenouseDataGen/Female/bruno-emmanuelle-Cm2rxFQ11xE-unsplash_nmpsi9.jpg', 
                       'https://res.cloudinary.com/safcloud/image/upload/v1606389506/TenouseDataGen/Female/sherise-Zh24qdeh1mE-unsplash_phs32n.jpg', 
                       'https://res.cloudinary.com/safcloud/image/upload/v1606389506/TenouseDataGen/Female/daniil-lobachev-yqJ0f1CCXso-unsplash_oghp5t.jpg', 
                       'https://res.cloudinary.com/safcloud/image/upload/v1606389506/TenouseDataGen/Female/daniil-kuzelev-TyomSa9Au1U-unsplash_xpowhl.jpg']
        
        self.roommate_pic = {
            'Male':self.male,
            'Female':self.female
            }
        
        self.roommate_question1 = ['Highly Focused', 'Often Partying/Hanging out', 'Focused as well as Hanging out', 'Neither Focused nor Hanging out']
        self.roommate_question2 = ['1-3', '4-6', '7-10', 'Cool with any']
        self.roommate_question3 = ['Student', 'Employee', 'Self Employed', 'Free Lancer', 'Tourist']
        self.roommate_question4 = ['Male', 'Female', 'Any']
        self.roommate_question5 = ['Student', 'Employee', 'Self Employed', 'Free Lancer', 'Tourist']
        self.roommate_question6 = ["Shouldn't consume alcohol or any harmful/illegal substance", "Cool with anything"]
        self.roommate_question7 = ['Married', 'Not Married']
        self.roommate_question8 = ['Married', 'Not Married']
        self.roommate_question9 = ['18', '21', '25', '30']
        self.roommate_question10 = ['Male', 'Female']
        self.roommate_question11 = ['18-25', '26-30', '31-45', '46-60', 'Cool with any']
        self.roommate_question12 = ['Pune', 'Mumbai', 'Bangalore', 'Hyderabad']
        self.roommate_question13 = ['I am a Engineer', 'I am a doctor', 'I am a student', 'I am here as a tourist']
        self.roommate_question14 = ['No']
        
        
        
    def house_data(self):
        print("-------------Generating House Data-------------------")
        
        house_struct = random.choice(self.house_struct)
        pic1 = random.choice(self.house_struct_obj[house_struct])
        
        house_type = random.choice(self.house_type)
        interior_pics = copy.deepcopy(self.house_type_obj[house_type])
        pic2 = random.choice(interior_pics)
        interior_pics.remove(pic2)
        pic3 = random.choice(interior_pics)
        
        question1 = random.choice(self.house_question1)
        question2 = random.choice(self.house_question2)
        question3 = random.choice(self.house_question3)
        question4 = random.choice(self.house_question4)
        question5 = random.choice(self.house_question5)
        question6 = random.choice(self.house_question6)
        question7 = self.house_question7[question6]
        question8 = random.choice(self.house_question8)
        question9 = self.house_question9[question6]
        
        print(house_struct)
        print(pic1)
        print(house_type)
        print(pic2)
        print(pic3)
        print(question1)
        print(question2)
        print(question3)
        print(question4)
        print(question5)
        print(question6)
        print(question7)
        print(question8)
        print(question9)
        
    def roommate_data(self):
        print("-----------Generating Roommate Data--------------")
        
        question1 = random.choice(self.roommate_question1)
        question2 = random.choice(self.roommate_question2)
        question3 = random.choice(self.roommate_question3)
        question4 = random.choice(self.roommate_question4)
        question5 = random.choice(self.roommate_question5)
        question6 = random.choice(self.roommate_question6)
        question7 = random.choice(self.roommate_question7)
        question8 = random.choice(self.roommate_question8)
        question9 = random.choice(self.roommate_question9)
        question10 = random.choice(self.roommate_question10)
        question11 = random.choice(self.roommate_question11)
        question12 = random.choice(self.roommate_question12)
        question13 = random.choice(self.roommate_question13)
        question14 = random.choice(self.roommate_question14)
        
        pic1 = random.choice(self.roommate_pic[question10])
        
        
        print(question1)
        print(question2)
        print(question3)
        print(question4)
        print(question5)
        print(question6)
        print(question7)
        print(question8)
        print(question9)
        print(question10)
        print(question11)
        print(question12)
        print(question13)
        print(question14)
        print(pic1)
        
    def user_data(self):
        print("-----------Generating Users--------------")
        alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        fnames = []
        lnames = []
        while(True):
            if(len(fnames)>11):
                break
            c1 = random.choice(alphas)
            c2 = random.choice(alphas).lower()
            c3 = random.choice(alphas).lower()
            c4 = random.choice(alphas).lower()
            c5 = random.choice(alphas).lower()
            fname = c1+c2+c3+c4+c5
            if fname not in fnames:
                fnames.append(fname)
        
        while(True):
           if(len(lnames)>11):
               break
           c1 = random.choice(alphas)
           c2 = random.choice(alphas).lower()
           c3 = random.choice(alphas).lower()
           c4 = random.choice(alphas).lower()
           c5 = random.choice(alphas).lower()
           lname = c1+c2+c3+c4+c5
           if lname not in lnames:
               lnames.append(lname)
        
        city = random.choice(self.house_question6)
        gender = random.choice(self.roommate_question10)
        pic = random.choice(self.roommate_pic[gender])
        password = fnames[4]
        
        print(fnames[4] + " " + lnames[4])
        print(city)
        print(gender)
        print(pic)
        print(password)
        
if __name__=='__main__':
    dg = DataGenerator()
    dg.house_data()
    dg.roommate_data()
    dg.user_data()
