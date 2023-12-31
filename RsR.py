import subprocess

class MyTool:
    def __init__(self, motor_id, robot_type):
        self.motor_id = motor_id
        self.data_dict = {}
        self.yml_dict = {}
        
        
        
        self.read_setup_data(self.motor_id)
        self.read_yml_data(self.yml_dict)
        
        # self.init_actual_data(self.motor_id)
        self.init_expected_data("ARM")
        
        # self.update_motor_data(self.motor_id)
    
        
        
    def read_yml_data(self,robot_type):
        #TODO: please implement yml parsing and use dictionary to stor it * 3
        #this function should pars data from yamls:
        #   1.mapping (joint params)
        #   2. NEW: correlate dof to motor type
        #   3. NEW: correlate dof to abs enc type (TBD)
        pass
        
    
    # def read_setup_data(self, object_id):
    # # Define the command with the object ID as a variable
    #     command = f"mdtool setup info {object_id}"

    #     try:
    #         # Execute the command and capture the output
    #         output = subprocess.check_output(command, shell=True, text=True)

    #         # Split the output by lines and parse each line
    #         for line in output.splitlines():
    #             # Split each line by ":" to separate key and value
    #             parts = line.strip().split(":")
    #             if len(parts) == 2:
    #                 key = parts[0].strip()
    #                 key=key.lstrip("- ")
    #                 value = parts[1].strip()
    #                 self.data_dict[key] = value
    #     except subprocess.CalledProcessError as e:
    #         print(f"Error executing command: {e}")
            
    #     # for key, value in self.data_dict.items():
    #     #     print(f"key:{key}")
    #     #     print(f"val: {value}")
    #     #     print("#################")
        
    #     #clean unnecessary chars after automated parser
 
    def read_setup_data(self, object_id):
        # Define the command with the object ID as a variable
        command = f"mdtool setup info {object_id}"

        try:
            # Execute the command and capture the output
            output = subprocess.check_output(command, shell=True, text=True)

            # Split the output by lines and parse each line
            for line in output.splitlines():
                # Split each line by ":" to separate key and value
                parts = line.strip().split(":")
                if len(parts) == 2:
                    key = parts[0].strip()
                    key =key.lstrip("[MDTOOL]")
                    key =key.lstrip("[CANDLE]")
                    key =key.lstrip("- ")
                    value = parts[1].strip()
                    self.data_dict[key] = value

            # Create class attributes from data_dict keys
            for key, value in self.data_dict.items():
                setattr(self, key, value)

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
 
        

        
    # def init_actual_data(self, motor_id):
        
    #     # Initialize attributes with default values
    #     self.actuator_name = ""
    #     self.can_speed = ""
    #     self.can_termination_resistor = ""
    #     self.gear_ratio = ""
    #     self.firmware_version = ""
    #     self.hardware_version = ""
    #     self.build_date = ""
    #     self.commit_hash = ""
    #     self.max_current = ""
    #     self.bridge_type = ""
    #     self.shunt_resistance = ""
    #     self.pole_pairs = ""
    #     self.kv_rating = ""
    #     self.motor_shutdown_temperature = ""
    #     self.motor_calibration_mode = ""
    #     self.motor_torque_constant = ""
    #     self.motor_stiction = ""
    #     self.motor_friction = ""
    #     self.d_axis_resistance = ""
    #     self.d_axis_inductance = ""
    #     self.torque_bandwidth = ""
    #     self.can_watchdog = ""
    #     self.output_encoder = ""
    #     self.position = ""
    #     self.velocity = ""
    #     self.torque = ""
    #     self.mosfet_temperature = ""
    #     self.motor_temperature = ""
    #     self.main_encoder_error = ""
    #     self.calibration_error = ""
    #     self.bridge_error = ""
    #     self.hardware_error = ""
    #     self.communication_error = ""
        
    def update_motor_data(self, motor_id):
        # First, read the setup data into self.data_dict using read_setup_data
        self.read_setup_data(motor_id)
        
        # Then, iterate through the attributes in init_actual_data
        for attribute_name in dir(self):
            if not attribute_name.startswith("__") and attribute_name in self.data_dict:
                setattr(self, attribute_name, self.data_dict[attribute_name])

    
    def init_expected_data(self,robot_type): #type necessary?
        #this function should pars data from yamls:
        # 1.mapping (joint params)
        # 2. NEW: correlate dof to motor type = name = name in .cfg file (you can generate it from these files)
        # 3. NEW: correlate dof to abs enc type (TBD)
        if (robot_type=="LEG"):
            self.hip_yaw        =""
            self.hip_roll       =""
            self.hip_pitch      =""
            self.Knee           =""
            self.ankle_pitch    =""
            self.ankle_roll     =""
            
        elif (robot_type=="ARM"):
            self.shoulder_roll  =""
            self.shoulder_pitch =""
            self.shoulder_pitch =""
            self.elbow          =""
            self.wrist_pitch    ="" 
            self.wrist_yaw      ="" 
            self.wrist_roll     =""
        
        elif (robot_type=="ARNI"):
            #TBD
            print("")
        
        
    def error_reporter(self):
        #TODO: this function should extract errors from actual_data_dic and report them.
        # TBD: if any errors exist i would like to get notified abut it - let use our mail
        cnt = 222
        attributes_and_values = vars(self)
        for attr, value in attributes_and_values.items():
            if "error" in attr:
                if "ALL OK" not in value:
                    cnt=cnt+1
                    print ("OMG ERROR")
                else:
                    print (value)
        print(f"tot num of errors: {cnt}")
        
        # for attribute_name in dir(self):
        #     if not attribute_name.startswith("__") and attribute_name in self.data_dict:
        #         if "error" in attribute_name:
        #             print (attribute_name)
      
        
        pass
    
    def encoder_tracker(self,motor_id):
        #TODO: (TBD) this function should extract encoder position from actual_data_dic and store it into a google sheet so we can track it
        #TODO: we need to figure out a way to take in count when system was calibrated.
        pass
        
    def get_actuator_name(self):
        return self.actuator_name
        

###END OF CLASS###
    
def update_robo_state(self):
    #TODO: this function should execute all actions to each motor in a robot. 
    #it not a class function. its a function that automates class functions. 
    pass


def main():
    # Create an instance of the MyTool class
    single_motor = MyTool(200,"ARM")

    # # Use the class's method
    # print(f"this is actuator's {single_motor.motor_id} name: {single_motor.get_actuator_name()}!")

    attributes_and_values = vars(single_motor)

    # Print the attributes and their values
    for attr, value in attributes_and_values.items():
        if (attr!="data_dict"):
            print(f"{attr}: {value}")
            print("#### next ####")
            
    print("wdsda;lk")
    
    single_motor.error_reporter()

if __name__ == "__main__":
    main()

