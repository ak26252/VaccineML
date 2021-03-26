#Kunho Kim
#GAVEL Vaccine World Machine Learning

import pandas as pd
import numpy as np
import os
import math
import csv

#filename to be used
# path = r"GAVEL/VRdata.zip"
file = r"333.csv"
file_write = r"results.csv"
directory = r"VRdata"

#line separator
line = "-"*70

# os.chdir("GAVEL")

#this is to make printing have no limit so it's more informative
np.set_printoptions(precision=5)
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)

class vr_data:
    
    """
    method for reading the csv file
    """
    def read(self, filename):
        self.data = pd.read_csv(filename, header = 1)
        
        
    """
    Get user ID from filename
    """
    def get_id(self, filename):
        id = filename.split('.')[0:1]
        return id
        
    
    """
    method for getting the overall total head rotation
    """
    def get_total_rotation(self, label):
        
        #create correct indices to observe in dataframe
        start = 1
        end = len(self.data.index)
        
        #create list containing all 'Ry' values
        data_list = self.data[label].iloc[start:end].tolist()
        
        #initialize values (still a noob at python coming from java lmao)
        # index = 0
        # temp = 0.0
        # total = 0.0
        index = 0
        temp = 0.0
        total = 0.0
        scene_total = 0.0
        scene = 0
        scene_index = 0
        scene_arr = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        scene_arr_num = np.array([0, 0, 0, 0, 0])
        num_zero = 0
        
        #We find the difference between each frame and add to the total
        # for item in data_list:
        #     if index == 0:
        #         temp = item
        #         index += 1
        #         continue
        #     #ignore 0's and NaN's
        #     if (item == 0) or (np.isnan(item)):
        #         continue
        #     else:
        #         diff = abs(item - temp)
        #         total += diff
        #         temp = item
        #         index += 1
        for item in data_list:
            if index == 0:
                temp = item
                index += 1
                continue
            #ignore 0's
            if item == 0:
                num_zero += 1
                continue
            #new scene
            if (np.isnan(item)) or (index == end - 6 - num_zero):
                # print(scene+1, scene_total, scene_index, index)
                scene_arr[scene] = scene_total
                scene_arr_num[scene] = scene_index
                scene += 1
                scene_total = 0.0
                scene_index = 0
                continue
            else:
                diff = abs(item - temp)
                total += diff
                scene_total += diff
                temp = item
                index += 1
                scene_index += 1      
            
        arr = np.array([total, index - 2])
        
        if label == 'Ry':
            self.total_arr_ry = arr
            self.total_scene_ry = scene_arr
            self.num_scene_ry = scene_arr_num
        elif label == 'Rx':
            self.total_arr_rx = arr
            self.total_scene_rx = scene_arr
            self.num_scene_rx = scene_arr_num
        elif label == 'Rz':
            self.total_arr_rz = arr
            self.total_scene_rz = scene_arr
            self.num_scene_rz = scene_arr_num
    
        return arr[0]
    
    
    """
    method for getting the overall average ry
    """
    def ry_avg(self):
        
        arr = self.total_arr_ry
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting the overall average rx
    """
    def rx_avg(self):
        
        arr = self.total_arr_rx
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting the overall average rz
    """
    def rz_avg(self):
        
        arr = self.total_arr_rz
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting total ry per scene
    """
    def get_scene_ry_total(self):
        return self.total_scene_ry
    
    """
    method for getting total ry per scene
    """
    def get_scene_rx_total(self):
        return self.total_scene_rx
    
    """
    method for getting total ry per scene
    """
    def get_scene_rz_total(self):
        return self.total_scene_rz
    
    """
    method for average ry per scene
    """
    def get_scene_ry_average(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_ry:
            scene_avg[i] = self.total_scene_ry[i]/self.num_scene_ry[i]
            i += 1
            
        return scene_avg
    
    """
    method for average ry per scene
    """
    def get_scene_rx_average(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_rx:
            scene_avg[i] = self.total_scene_rx[i]/self.num_scene_rx[i]
            i += 1
            
        return scene_avg
    
    """
    method for average ry per scene
    """
    def get_scene_rz_average(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_rz:
            scene_avg[i] = self.total_scene_rz[i]/self.num_scene_rz[i]
            i += 1
            
        return scene_avg
    
    """
    method for getting the overall total distance traveled
    """
    def get_total_distance(self):
        
        #create correct indices to observe in dataframe
        start = 1
        end = len(self.data.index)
        
        #create list containing all 'Ry' values
        tx_list = self.data['Tx'].iloc[start:end].tolist()
        ty_list = self.data['Ty'].iloc[start:end].tolist()
        tz_list = self.data['Tz'].iloc[start:end].tolist()
        
        
        #initialize values (still a noob at python coming from java lmao)
        index = 0
        other_index = 0
        temp_tx = 0.0
        temp_ty = 0.0
        temp_tz = 0.0
        total = 0.0
        
        #We find the difference between each frame and add to the total
        for item in tx_list:
            if index == 0:
                temp_tx = item
                temp_ty = ty_list[0]
                temp_tz = tz_list[0]
                index += 1
                other_index += 1
                continue
            #ignore 0's and NaN's
            if (item == 0) or (np.isnan(item)) or (ty_list[other_index] == 0) or (tz_list[other_index] == 0) or (np.isnan(ty_list[other_index])) or (np.isnan(tz_list[other_index])):
                other_index += 1
                continue
            else:
                distance = math.sqrt(((temp_tx - item) ** 2) + ((temp_ty - ty_list[other_index]) ** 2) + ((temp_tz - tz_list[other_index]) ** 2))
                total += distance
                temp_tx = item
                temp_ty = ty_list[other_index]
                temp_tz = tz_list[other_index]
                index += 1
                other_index += 1
            
        arr = np.array([total, index - 2])
        
        self.total_arr_distance = arr
    
        return arr[0]
  
    """
    method for getting the overall average distance
    """
    def distance_avg(self):
        
        arr = self.total_arr_distance
        avg = arr[0] / arr[1]
        
        return avg
    
"""
Write to csv file
"""
with open(file_write, 'w', newline = '') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    
    #A = average, T = total
    fields = ['ID','Ry Tot','Ry Avg','Rx Tot','Rx Avg','Rz Tot','Rz Avg','Rot Tot','Rot Avg','Dist Tot','Dis Avg','S1Rot Tot','S1Rot Avg','S2Rot Tot','S2Rot Avg','S3Rot Tot','S3Rot Avg','S4Rot Tot','S4Rot Avg','S5Rot Tot','S5Rot Avg']
    csvwriter.writerow(fields)

    file_list = []
        
    results = [] 
        
    files = os.listdir(directory)
    
    os.chdir(directory)
    
    for file in files:
        file_list.append(file)
    
    for fname in file_list:
        vr_data()  
        vr = vr_data()
        vr.read(fname)
        uid = ' '.join(vr.get_id(fname))
        ry_total = vr.get_total_rotation('Ry')
        ry_avg = vr.ry_avg()
        rx_total = vr.get_total_rotation('Rx')
        rx_avg = vr.rx_avg()
        rz_total = vr.get_total_rotation('Rz')
        rz_avg = vr.rz_avg()
        rot_total = ry_total + rx_total + rz_total
        rot_avg_total = ry_avg + rx_avg + rz_avg
        distance_total = vr.get_total_distance()
        distance_avg = vr.distance_avg()
        
        #total and average by rotation axis
        sRy_total = vr.get_scene_ry_total()
        sRy_avg = vr.get_scene_ry_average()
        sRx_total = vr.get_scene_rx_total()
        sRx_avg = vr.get_scene_rx_average()
        sRz_total = vr.get_scene_rz_total()
        sRz_avg = vr.get_scene_rz_average()
        
        #total by scene
        s1_rot_tot = sRy_total[0] + sRx_total[0] + sRz_total[0]
        s2_rot_tot = sRy_total[1] + sRx_total[1] + sRz_total[1]
        s3_rot_tot = sRy_total[2] + sRx_total[2] + sRz_total[2]
        s4_rot_tot = sRy_total[3] + sRx_total[3] + sRz_total[3]
        s5_rot_tot = sRy_total[4] + sRx_total[4] + sRz_total[4]
        
        #average by scene
        s1_rot_avg = sRy_avg[0] + sRx_avg[0] + sRz_avg[0]
        s2_rot_avg = sRy_avg[1] + sRx_avg[1] + sRz_avg[1]
        s3_rot_avg = sRy_avg[2] + sRx_avg[2] + sRz_avg[2]
        s4_rot_avg = sRy_avg[3] + sRx_avg[3] + sRz_avg[3]
        s5_rot_avg = sRy_avg[4] + sRx_avg[4] + sRz_avg[4]
        
        #convert s4 and s5 average nan values to 0
        if np.isnan(s4_rot_avg):
            s4_rot_avg = 0
        if np.isnan(s5_rot_avg):
            s5_rot_avg = 0
        
        row = [uid, ry_total, ry_avg, rx_total, rx_avg, rz_total, rz_avg, rot_total, rot_avg_total, distance_total, distance_avg, s1_rot_tot, s1_rot_avg, s2_rot_tot, s2_rot_avg, s3_rot_tot, s3_rot_avg, s4_rot_tot, s4_rot_avg, s5_rot_tot, s5_rot_avg]
        results.append(row)
        
       
        
    csvwriter.writerows(results)

