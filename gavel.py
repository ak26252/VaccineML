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
        self.id = id
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
        
        # print("Id:", self.id)
        
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
            if (scene >= 5):
                break
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
        
        #Head
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
            
        #Left hand    
        elif label == 'LeftRy':
            self.total_arr_ry_LH = arr
            self.total_scene_ry_LH = scene_arr
            self.num_scene_ry_LH = scene_arr_num
        elif label == 'LeftRx':
            self.total_arr_rx_LH = arr
            self.total_scene_rx_LH = scene_arr
            self.num_scene_rx_LH = scene_arr_num
        elif label == 'LeftRz':
            self.total_arr_rz_LH = arr
            self.total_scene_rz_LH = scene_arr
            self.num_scene_rz_LH = scene_arr_num   
            
        #Right hand
        elif label == 'RightRy':
            self.total_arr_ry_RH = arr
            self.total_scene_ry_RH = scene_arr
            self.num_scene_ry_RH = scene_arr_num
        elif label == 'RightRx':
            self.total_arr_rx_RH = arr
            self.total_scene_rx_RH = scene_arr
            self.num_scene_rx_RH = scene_arr_num
        elif label == 'RightRz':
            self.total_arr_rz_RH = arr
            self.total_scene_rz_RH = scene_arr
            self.num_scene_rz_RH = scene_arr_num
            
    
        return arr[0]
    
    
    """
    method for getting the overall average ry
    """
    def ry_avg(self, label):
        if label == "head":
            arr = self.total_arr_ry
        elif label == "LH":
            arr = self.total_arr_ry_LH
        elif label == "RH":
            arr = self.total_arr_ry_RH
        
        arr = self.total_arr_ry
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting the overall average rx
    """
    def rx_avg(self, label):
        if label == "head":
            arr = self.total_arr_rx
        elif label == "LH":
            arr = self.total_arr_rx_LH
        elif label == "RH":
            arr = self.total_arr_rx_RH
        
        arr = self.total_arr_rx
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting the overall average rz
    """
    def rz_avg(self, label):
        if label == "head":
            arr = self.total_arr_rz
        elif label == "LH":
            arr = self.total_arr_rz_LH
        elif label == "RH":
            arr = self.total_arr_rz_RH
        
        arr = self.total_arr_rz
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting total ry per scene
    """
    def get_scene_ry_total(self, label):
        if label == "head":
            arr = self.total_scene_ry
        elif label == "LH":
            arr = self.total_scene_ry_LH
        elif label == "RH":
            arr = self.total_scene_ry_RH
        
        return arr
    
    """
    method for getting total ry per scene
    """
    def get_scene_rx_total(self, label):
        if label == "head":
            arr = self.total_scene_rx
        elif label == "LH":
            arr = self.total_scene_rx_LH
        elif label == "RH":
            arr = self.total_scene_rx_RH
        
        return arr
    
    """
    method for getting total ry per scene
    """
    def get_scene_rz_total(self, label):
        if label == "head":
            arr = self.total_scene_rz
        elif label == "LH":
            arr = self.total_scene_rz_LH
        elif label == "RH":
            arr = self.total_scene_rz_RH
        
        return arr
    
    """
    method for average ry per scene
    """
    def get_scene_ry_average(self, label):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        if label == "head":
            arr = self.total_scene_ry
            arrNum = self.num_scene_ry
        elif label == "LH":
            arr = self.total_scene_ry_LH
            arrNum = self.num_scene_ry_LH
        elif label == "RH":
            arr = self.total_scene_ry_RH
            arrNum = self.num_scene_ry_RH
            
        for item in arr:
            scene_avg[i] = arr[i]/arrNum[i]
            i += 1
            
        return scene_avg
    
    """
    method for average ry per scene
    """
    def get_scene_rx_average(self, label):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        if label == "head":
            arr = self.total_scene_rx
            arrNum = self.num_scene_rx
        elif label == "LH":
            arr = self.total_scene_rx_LH
            arrNum = self.num_scene_rx_LH
        elif label == "RH":
            arr = self.total_scene_rx_RH
            arrNum = self.num_scene_rx_RH
            
        for item in arr:
            scene_avg[i] = arr[i]/arrNum[i]
            i += 1
            
        return scene_avg
    
    """
    method for average ry per scene
    """
    def get_scene_rz_average(self, label):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        if label == "head":
            arr = self.total_scene_rz
            arrNum = self.num_scene_rz
        elif label == "LH":
            arr = self.total_scene_rz_LH
            arrNum = self.num_scene_rz_LH
        elif label == "RH":
            arr = self.total_scene_rz_RH
            arrNum = self.num_scene_rz_RH
            
        for item in arr:
            scene_avg[i] = arr[i]/arrNum[i]
            i += 1
            
        return scene_avg
    
    """
    method for getting the overall total distance traveled
    """
    def get_total_distance(self, typeStr):
        
        #create correct indices to observe in dataframe
        start = 1
        end = len(self.data.index)
        
        if typeStr == "head":
            #create list containing all 'Ry' values
            tx_list = self.data['Tx'].iloc[start:end].tolist()
            ty_list = self.data['Ty'].iloc[start:end].tolist()
            tz_list = self.data['Tz'].iloc[start:end].tolist()
        elif typeStr == "LH":
            tx_list = self.data['LeftTx'].iloc[start:end].tolist()
            ty_list = self.data['LeftTy'].iloc[start:end].tolist()
            tz_list = self.data['LeftTz'].iloc[start:end].tolist()
        elif typeStr == "RH":
            tx_list = self.data['RightTx'].iloc[start:end].tolist()
            ty_list = self.data['RightTy'].iloc[start:end].tolist()
            tz_list = self.data['RightTz'].iloc[start:end].tolist()
        
        
        #initialize values (still a noob at python coming from java lmao)
        index = 0
        other_index = 0
        temp_tx = 0.0
        temp_ty = 0.0
        temp_tz = 0.0
        total = 0.0
        scene_total = 0.0
        scene = 0
        scene_index = 0
        scene_arr = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        scene_arr_num = np.array([0, 0, 0, 0, 0])
        num_zero = 0
        
        #We find the difference between each frame and add to the total
        for item in tx_list:
            # print(scene_total)
            if index == 0:
                temp_tx = item
                temp_ty = ty_list[0]
                temp_tz = tz_list[0]
                index += 1
                other_index += 1
                continue
            if (scene >= 5):
                break
            if ((item == 0) or (ty_list[other_index] == 0) or (tz_list[other_index] == 0)):
                num_zero += 1
                # print("numzero:", num_zero)
                continue
            #ignore 0's and NaN's
            if (np.isnan(item)) or (np.isnan(ty_list[other_index])) or (np.isnan(tz_list[other_index])) or (other_index == end - 6 - num_zero):
                # print("here")
                print(scene_total)
                scene_arr[scene] = scene_total
                # print(scene_total)
                scene_arr_num[scene] = scene_index
                scene += 1
                scene_total = 0.0
                # other_index += 1
                scene_index = 0
                
                continue
            else:
                distance = math.sqrt(((temp_tx - item) ** 2) + ((temp_ty - ty_list[other_index]) ** 2) + ((temp_tz - tz_list[other_index]) ** 2))
                total += distance
                scene_total += distance
                temp_tx = item
                temp_ty = ty_list[other_index]
                temp_tz = tz_list[other_index]
                index += 1
                other_index += 1
                scene_index += 1
                # print(scene_total)
            
        arr = np.array([total, index - 2])
        
        if typeStr == "head":
            self.total_arr_distance = arr
            self.total_scene_distance = scene_arr
            self.num_scene_distance = scene_arr_num
        elif typeStr == "LH":
            # print(scene_arr)
            self.total_arr_distance_LH = arr
            self.total_scene_distance_LH = scene_arr
            self.num_scene_distance_LH = scene_arr_num
        elif typeStr == "RH":
            self.total_arr_distance_RH = arr
            self.total_scene_distance_RH = scene_arr
            self.num_scene_distance_RH = scene_arr_num
        
    
        
        return arr[0]
  
    """
    method for getting the overall average distance
    """
    def distance_avg(self, label):
        if label == "head":
            arr = self.total_arr_distance
        elif label == "LH":
            arr = self.total_arr_distance_LH
        elif label == "RH":
            arr = self.total_arr_distance_RH
            
        avg = arr[0] / arr[1]
        
        return avg
    
    """
    method for getting scene distance of head
    """
    def get_scene_distance(self):
        return self.total_scene_distance
    
    """
    method for getting scene distance of LH
    """
    def get_scene_distance_LH(self):
        return self.total_scene_distance_LH
    
    """
    method for getting scene distance of RH
    """
    def get_scene_distance_RH(self):
        return self.total_scene_distance_RH
    
    """
    method for getting scene distance average of head
    """
    def get_scene_distance_avg(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_distance:
            scene_avg[i] = self.total_scene_distance[i]/self.num_scene_distance[i]
            i += 1
            
        return scene_avg
    
    """
    method for getting scene distance average of head
    """
    def get_scene_distance_avg_LH(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_distance_LH:
            scene_avg[i] = self.total_scene_distance_LH[i]/self.num_scene_distance_LH[i]
            i += 1
            
        return scene_avg
    
    """
    method for getting scene distance average of head
    """
    def get_scene_distance_avg_RH(self):
        scene_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0

        for item in self.total_scene_distance_RH:
            scene_avg[i] = self.total_scene_distance_RH[i]/self.num_scene_distance_RH[i]
            i += 1
            
        return scene_avg
    
"""
Write to csv file
"""
with open(file_write, 'w', newline = '') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    
    #A = average, T = total
    fields = ['ID','Ry Tot','Ry Avg','Rx Tot','Rx Avg','Rz Tot','Rz Avg','Rot Tot','Rot Avg','Dist Tot','Dis Avg','S1Rot Tot','S1Rot Avg','S2Rot Tot','S2Rot Avg','S3Rot Tot','S3Rot Avg','S4Rot Tot','S4Rot Avg','S5Rot Tot','S5Rot Avg', 'S1Dist Tot', 'S1Dist Avg', 'S2Dist Tot', 'S2Dist Avg', 'S3Dist Tot', 'S3Dist Avg', 'S4Dist Tot', 'S4Dist Avg', 'S5Dist Tot', 'S5Dist Avg', 'LH Ry Tot','LH Ry Avg','LH Rx Tot','LH Rx Avg','LH Rz Tot','LH Rz Avg','LH Rot Tot','LH Rot Avg','LH Dist Tot','LH Dis Avg','LH S1Rot Tot','LH S1Rot Avg','LH S2Rot Tot','LH S2Rot Avg','LH S3Rot Tot','LH S3Rot Avg','LH S4Rot Tot','LH S4Rot Avg','LH S5Rot Tot','LH S5Rot Avg', 'LH S1Dist Tot', 'LH S1Dist Avg', 'LH S2Dist Tot', 'LH S2Dist Avg', 'LH S3Dist Tot', 'LH S3Dist Avg', 'LH S4Dist Tot', 'LH S4Dist Avg', 'LH S5Dist Tot', 'LH S5Dist Avg', 'RH Ry Tot','RH Ry Avg','RH Rx Tot','RH Rx Avg','RH Rz Tot','RH Rz Avg','RH Rot Tot','RH Rot Avg','RH Dist Tot','RH Dis Avg','RH S1Rot Tot','RH S1Rot Avg','RH S2Rot Tot','RH S2Rot Avg','RH S3Rot Tot','RH S3Rot Avg','RH S4Rot Tot','RH S4Rot Avg','RH S5Rot Tot','RH S5Rot Avg', 'RH S1Dist Tot', 'RH S1Dist Avg', 'RH S2Dist Tot', 'RH S2Dist Avg', 'RH S3Dist Tot', 'RH S3Dist Avg', 'RH S4Dist Tot', 'RH S4Dist Avg', 'RH S5Dist Tot', 'RH S5Dist Avg']
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
        
        #head rotation
        ry_total = vr.get_total_rotation('Ry')
        ry_avg = vr.ry_avg('head')
        rx_total = vr.get_total_rotation('Rx')
        rx_avg = vr.rx_avg('head')
        rz_total = vr.get_total_rotation('Rz')
        rz_avg = vr.rz_avg('head')
        rot_total = ry_total + rx_total + rz_total
        rot_avg_total = ry_avg + rx_avg + rz_avg
        
        #total and average by rotation axis
        sRy_total = vr.get_scene_ry_total('head')
        sRy_avg = vr.get_scene_ry_average('head')
        sRx_total = vr.get_scene_rx_total('head')
        sRx_avg = vr.get_scene_rx_average('head')
        sRz_total = vr.get_scene_rz_total('head')
        sRz_avg = vr.get_scene_rz_average('head')
        
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
        
        #LH rotation
        ry_total_LH = vr.get_total_rotation('LeftRy')
        ry_avg_LH = vr.ry_avg('LH')
        rx_total_LH = vr.get_total_rotation('LeftRx')
        rx_avg_LH = vr.rx_avg('LH')
        rz_total_LH = vr.get_total_rotation('LeftRz')
        rz_avg_LH = vr.rz_avg('LH')
        rot_total_LH = ry_total + rx_total + rz_total
        rot_avg_total_LH = ry_avg + rx_avg + rz_avg
        
        #total and average by rotation axis
        sRy_total_LH = vr.get_scene_ry_total('LH')
        sRy_avg_LH = vr.get_scene_ry_average('LH')
        sRx_total_LH = vr.get_scene_rx_total('LH')
        sRx_avg_LH = vr.get_scene_rx_average('LH')
        sRz_total_LH = vr.get_scene_rz_total('LH')
        sRz_avg_LH = vr.get_scene_rz_average('LH')
        
        #total by scene
        s1_rot_tot_LH = sRy_total_LH[0] + sRx_total_LH[0] + sRz_total_LH[0]
        s2_rot_tot_LH = sRy_total_LH[1] + sRx_total_LH[1] + sRz_total_LH[1]
        s3_rot_tot_LH = sRy_total_LH[2] + sRx_total_LH[2] + sRz_total_LH[2]
        s4_rot_tot_LH = sRy_total_LH[3] + sRx_total_LH[3] + sRz_total_LH[3]
        s5_rot_tot_LH = sRy_total_LH[4] + sRx_total_LH[4] + sRz_total_LH[4]
        
        #average by scene
        s1_rot_avg_LH = sRy_avg_LH[0] + sRx_avg_LH[0] + sRz_avg_LH[0]
        s2_rot_avg_LH = sRy_avg_LH[1] + sRx_avg_LH[1] + sRz_avg_LH[1]
        s3_rot_avg_LH = sRy_avg_LH[2] + sRx_avg_LH[2] + sRz_avg_LH[2]
        s4_rot_avg_LH = sRy_avg_LH[3] + sRx_avg_LH[3] + sRz_avg_LH[3]
        s5_rot_avg_LH = sRy_avg_LH[4] + sRx_avg_LH[4] + sRz_avg_LH[4]
        
        
        #RH rotation
        ry_total_RH = vr.get_total_rotation('RightRy')
        ry_avg_RH = vr.ry_avg('RH')
        rx_total_RH = vr.get_total_rotation('RightRx')
        rx_avg_RH = vr.rx_avg('RH')
        rz_total_RH = vr.get_total_rotation('RightRz')
        rz_avg_RH = vr.rz_avg('RH')
        rot_total_RH = ry_total + rx_total + rz_total
        rot_avg_total_RH = ry_avg + rx_avg + rz_avg
        
        #total and average by rotation axis
        sRy_total_RH = vr.get_scene_ry_total('RH')
        sRy_avg_RH = vr.get_scene_ry_average('RH')
        sRx_total_RH = vr.get_scene_rx_total('RH')
        sRx_avg_RH = vr.get_scene_rx_average('RH')
        sRz_total_RH = vr.get_scene_rz_total('RH')
        sRz_avg_RH = vr.get_scene_rz_average('RH')
        
        #total by scene
        s1_rot_tot_RH = sRy_total_RH[0] + sRx_total_RH[0] + sRz_total_RH[0]
        s2_rot_tot_RH = sRy_total_RH[1] + sRx_total_RH[1] + sRz_total_RH[1]
        s3_rot_tot_RH = sRy_total_RH[2] + sRx_total_RH[2] + sRz_total_RH[2]
        s4_rot_tot_RH = sRy_total_RH[3] + sRx_total_RH[3] + sRz_total_RH[3]
        s5_rot_tot_RH = sRy_total_RH[4] + sRx_total_RH[4] + sRz_total_RH[4]
        
        #average by scene
        s1_rot_avg_RH = sRy_avg_RH[0] + sRx_avg_RH[0] + sRz_avg_RH[0]
        s2_rot_avg_RH = sRy_avg_RH[1] + sRx_avg_RH[1] + sRz_avg_RH[1]
        s3_rot_avg_RH = sRy_avg_RH[2] + sRx_avg_RH[2] + sRz_avg_RH[2]
        s4_rot_avg_RH = sRy_avg_RH[3] + sRx_avg_RH[3] + sRz_avg_RH[3]
        s5_rot_avg_RH = sRy_avg_RH[4] + sRx_avg_RH[4] + sRz_avg_RH[4]
        
     
            
        #Head distance
        distance_total = vr.get_total_distance('head')
        distance_avg = vr.distance_avg('head')
        dist_scene_total = vr.get_scene_distance()
        dist_scene_avg = vr.get_scene_distance_avg()
        
        s1_dist = dist_scene_total[0]
        s2_dist = dist_scene_total[1]
        s3_dist = dist_scene_total[2]
        s4_dist = dist_scene_total[3]
        s5_dist = dist_scene_total[4]
        
        s1_dist_avg = dist_scene_avg[0]
        s2_dist_avg = dist_scene_avg[1]
        s3_dist_avg = dist_scene_avg[2]
        s4_dist_avg = dist_scene_avg[3]
        s5_dist_avg = dist_scene_avg[4]
        
        #LH distance
        distance_total_LH = vr.get_total_distance('LH')
        distance_avg_LH = vr.distance_avg('LH')
        dist_scene_total_LH = vr.get_scene_distance_LH()
        dist_scene_avg_LH = vr.get_scene_distance_avg_LH()
        
        s1_dist_LH = dist_scene_total_LH[0]
        s2_dist_LH = dist_scene_total_LH[1]
        s3_dist_LH = dist_scene_total_LH[2]
        s4_dist_LH = dist_scene_total_LH[3]
        s5_dist_LH = dist_scene_total_LH[4]
        
        s1_dist_avg_LH = dist_scene_avg_LH[0]
        s2_dist_avg_LH = dist_scene_avg_LH[1]
        s3_dist_avg_LH = dist_scene_avg_LH[2]
        s4_dist_avg_LH = dist_scene_avg_LH[3]
        s5_dist_avg_LH = dist_scene_avg_LH[4]
        
        #RH distance
        distance_total_RH = vr.get_total_distance('RH')
        distance_avg_RH = vr.distance_avg('RH')
        dist_scene_total_RH = vr.get_scene_distance_RH()
        dist_scene_avg_RH = vr.get_scene_distance_avg_RH()
        
        s1_dist_RH = dist_scene_total_RH[0]
        s2_dist_RH = dist_scene_total_RH[1]
        s3_dist_RH = dist_scene_total_RH[2]
        s4_dist_RH = dist_scene_total_RH[3]
        s5_dist_RH = dist_scene_total_RH[4]
        
        s1_dist_avg_RH = dist_scene_avg_RH[0]
        s2_dist_avg_RH = dist_scene_avg_RH[1]
        s3_dist_avg_RH = dist_scene_avg_RH[2]
        s4_dist_avg_RH = dist_scene_avg_RH[3]
        s5_dist_avg_RH = dist_scene_avg_RH[4]
        
        row= [uid, ry_total, ry_avg, rx_total, rx_avg, rz_total, rz_avg, rot_total, rot_avg_total, distance_total, distance_avg, s1_rot_tot, s1_rot_avg, s2_rot_tot, s2_rot_avg, s3_rot_tot, s3_rot_avg, s4_rot_tot, s4_rot_avg, s5_rot_tot, s5_rot_avg, s1_dist, s1_dist_avg, s2_dist, s2_dist_avg, s3_dist, s3_dist_avg, s4_dist, s4_dist_avg, s5_dist, s5_dist_avg, ry_total_LH, ry_avg_LH, rx_total_LH, rx_avg_LH, rz_total_LH, rz_avg_LH, rot_total_LH, rot_avg_total_LH, distance_total_LH, distance_avg_LH, s1_rot_tot_LH, s1_rot_avg_LH, s2_rot_tot_LH, s2_rot_avg_LH, s3_rot_tot_LH, s3_rot_avg_LH, s4_rot_tot_LH, s4_rot_avg_LH, s5_rot_tot_LH, s5_rot_avg_LH, s1_dist_LH, s1_dist_avg_LH, s2_dist_LH, s2_dist_avg_LH, s3_dist_LH, s3_dist_avg_LH, s4_dist_LH, s4_dist_avg_LH, s5_dist_LH, s5_dist_avg_LH, ry_total_RH, ry_avg_RH, rx_total_RH, rx_avg_RH, rz_total_RH, rz_avg_RH, rot_total_RH, rot_avg_total_RH, distance_total_RH, distance_avg_RH, s1_rot_tot_RH, s1_rot_avg_RH, s2_rot_tot_RH, s2_rot_avg_RH, s3_rot_tot_RH, s3_rot_avg_RH, s4_rot_tot_RH, s4_rot_avg_RH, s5_rot_tot_RH, s5_rot_avg_RH, s1_dist_RH, s1_dist_avg_RH, s2_dist_RH, s2_dist_avg_RH, s3_dist_RH, s3_dist_avg_RH, s4_dist_RH, s4_dist_avg_RH, s5_dist_RH, s5_dist_avg_RH]
        #nan values to 0
        # for item in row:
        #     if np.isnan(item):
        #         item = 0
        results.append(row)
        
        
       
        
    csvwriter.writerows(results)

