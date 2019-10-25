import pandas as pd
import numpy as np

class Calculator:
    '''
    The calculator class collects information from all subclasses:
    Transport, Home Energe, Stuff
    '''
    def __init__(self, carbon_first_actual_avg, carbon_mid_avg, carbon_latest_rolling_avg):
        self.carbon_first_actual_avg = carbon_first_actual_avg
        self.carbon_mid_avg = carbon_mid_avg
        self.carbon_latest_rolling_avg = carbon_latest_rolling_avg

        # TODO: the dates should not be hard-coded but dynamically
        # taken from when the user accesses the app & latest year
        self.start_of_actual_data = 2018
        self.start_of_latest_actual_rolling_avg = 2021


        self.total_warming = None

        # Create the table that is in Calcs 350
        # rows are data entries for each year
        # columns are vehicle/ energy type etc.
        # columns are created as they are computed below

        columns = ['year']
        years = list(range(2016, 2065))
        self.overview_table = pd.DataFrame(columns = columns)
        self.overview_table.year = years




##########################################
# Transport
##########################################

class Transport(Calculator):
    def __init__(self, carbon_use):
        self.transport_warming = None
        self.carbon_use = carbon_use

    def get_warming(self):
        '''
        Returns the aggregate warming for the transport category.
        '''
        return


class Vehicle1_fossil(Transport):
    def __init__(self):
        return

    def get_cost(self, data):
        if data['year'] <= self.start_of_actual_data:
            return self.carbon_first_actual_avg
        elif data['year'] >= self.start_of_latest_actual_rolling_avg:
            return self.carbon_latest_rolling_avg
        else:  # in between
            return self.carbon_mid_avg


    def fill_overview_table(self):
        self.overview_table['Vehicle1_fossil'] = self.overview_table.apply(self.get_cost, axis=1)
        return








##########################################
# ONLY WORKED UNTIL HERE
##########################################




class Vehicle1_electric(Transport):
    def __init__(self):
        return


class Vehicle2_fossil(Transport):
    def __init__(self):
        return


class Vehicle2_electric(Transport):
    def __init__(self):
        return


class Bus(Transport):
    def __init__(self):
        return


class Train(Transport):
    def __init__(self):
        return


class Flight(Transport):
    def __init__(self):
        return


##########################################
# Home Energy
##########################################

class HomeEnergy(Calculator):
    def __init__(self):
        self.homeenergy_warming = None

    def get_warming(self, category):
        return 0


##########################################
# Stuff
##########################################

class Stuff(Calculator):
    def __init__(self):
        self.stuff_warming = None

    def get_warming(self, category):
        return 0
