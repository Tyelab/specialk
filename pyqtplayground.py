# Team Specialk Surgery Metadata Generation
# Jeremy Delahanty September 2021

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# from ruamel.yaml import YAML

from pathlib import Path

server_basepath = Path("X:/")

app = QApplication(sys.argv)

# 3 types of window to use: Q widget, q main window, q dialog

window = QMainWindow()
window.statusBar().showMessage("Hello, Surgeon! Welcome to Scalpel")
window.menuBar().addMenu("Test")

window.show()

sys.exit(app.exec())

# Complete surgery method to be linked into scalpel.py after ui update 11/3/21
    def complete_surgery(self):

        # Get Skull Leveling values
        bregma_pos = self.bregma_val
        lambda_pos = self.lambda_val
        level_left_pos = self.level_left_val
        level_right_pos = self.level_right_val

        # Get GRIN Lens positions
        grin_hemisphere = self.grin_hs_val
        grin_target = self.grin_target_val

        try:
            grin_ap = float(self.grin_ap_val)
            grin_ml = float(self.grin_ml_val)
            grin_dv = float(self.grin_dv_val)
            grin_angle = float(self.grin_angle_val)
        
        except TypeError:
            grin_ap = None
            grin_ml = None
            grin_dv = None
            grin_angle = None
        
        grin_notes = self.grin_notes

        # Get GCaMP Values
        gcamp_type = self.gcamp_type_val
        gcamp_hemisphere = self.gcamp_hs_val
        gcamp_target = self.gcamp_target_val

        try:
            gcamp_ap = float(self.gcamp_ap_val)
            gcamp_ml = float(self.gcamp_ml_val)
            gcamp_dv = float(self.gcamp_dv_val)
            gcamp_angle = float(self.gcamp_angle_val)
            gcamp_vol = float(self.gcamp_vol_val)
            gcamp_rate = float(self.gcamp_rate_val)

        except TypeError:
            gcamp_ap = None
            gcamp_ml = None
            gcamp_dv = None
            gcamp_angle = None
            gcamp_vol = None
            gcamp_rate = None

        gcamp_bevel = self.gcamp_bevel_val

        # Get Channel Rhodopsin Values

        chr_type = self.chr_type_val
        chr_hemisphere = self.chr_hs_val
        chr_target = self.chr_target_val

        try:
            chr_ap = float(self.chr_ap_val)
            chr_ml = float(self.chr_ml_val)
            chr_dv = float(self.chr_dv_val)
            chr_angle = float(self.chr_angle_val)
            chr_vol = float(self.chr_vol_val)
            chr_rate = float(self.chr_rate_val)
        
        except TypeError:
            chr_ap = None
            chr_ml = None
            chr_dv = None
            chr_angle = None
            chr_vol = None
            chr_rate = None
        
        chr_bevel = self.chr_bevel_val

        # Get Tracer Values

        tracer_type = self.tracer_type_val
        tracer_hemisphere = self.tracer_hs_val
        tracer_target = self.tracer_target_val

        try:
            tracer_ap = float(self.tracer_ap_val)
            tracer_ml = float(self.tracer_ml_val)
            tracer_dv = float(self.tracer_dv_val)
            tracer_angle = float(self.tracer_angle_val)
            tracer_vol = float(self.tracer_vol_val)
            tracer_rate = float(self.tracer_rate_val)
        
        except TypeError:
            tracer_ap = None
            tracer_ml = None
            tracer_dv = None
            tracer_angle = None
            tracer_vol = None
        
        tracer_bevel = self.tracer_bevel_val

        # Get headplate information
        num_screws = float(self.hp_screws_val)
        skull_hash = self.hp_hashing_val
        headplate_notes = self.hp_notes
        

        # Get surgeon information
        surgeon = self.surgeon_val
        stereotax = self.stereotax_val

        # Get patient information
        subject_id = self.patient_val
        subject_alias = self.alias_val
        subject_weight = self.weight_val
        subject_description = self.purpose

        # Get start and stop times
        start_time = dt_parser.parse(self.start_time)
        start_time = start_time.replace(tzinfo=tzlocal())
        end_time = dt_parser.parse(self.finish_time)
        end_time = end_time.replace(tzinfo=tzlocal())