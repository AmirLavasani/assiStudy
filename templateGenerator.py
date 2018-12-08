# -*- coding: utf-8 -*-
'''
    This class will help to build a result page
'''
from json2html import *


class TemplateGenerator:
    def __init__(self):
        self.page_template = u'<!DOCTYPE html> \
            <html lang="en"> \
            <head> \
                <title>AssiStudy</title> \
                <meta charset="UTF-8"> \
                <meta name="viewport" co ntent="width=device-width, initial-scale=1"> \
            <!--===============================================================================================--> \
                <link rel="icon" type="image/png" href="/static/images/icons/favicon.ico"/> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/bootstrap/css/bootstrap.min.css">  \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/fonts/font-awesome-4.7.0/css/font-awesome.min.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/animate/animate.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/css-hamburgers/hamburgers.min.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/animsition/css/animsition.min.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/select2/select2.min.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/vendor/daterangepicker/daterangepicker.css"> \
            <!--===============================================================================================--> \
                <link rel="stylesheet" type="text/css" href="/static/css/util.css"> \
                <link rel="stylesheet" type="text/css" href="/static/css/main.css"> \
            <!--===============================================================================================--> \
            </head> \
            <body> \
                <div class="container-contact100"> \
                    <div class="wrap-contact100"> \
                        <div>\
                        {} \
                        </div> \
                    </div> \
                </div> \
                <div id="dropDownSelect1"></div> \
            <!--===============================================================================================--> \
                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script> \
                <script src="/static/vendor/jquery/jquery-3.2.1.min.js"></script> \
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script> \
            <!--===============================================================================================--> \
                <script src="/static/vendor/animsition/js/animsition.min.js"></script> \
            <!--===============================================================================================--> \
                <script src="/static/vendor/bootstrap/js/popper.js"></script> \
                <script src="/static/vendor/bootstrap/js/bootstrap.min.js"></script> \
            <!--===============================================================================================--> \
            <!--===============================================================================================--> \
                <script src="/static/vendor/daterangepicker/moment.min.js"></script> \
                <script src="/static/vendor/daterangepicker/daterangepicker.js"></script> \
            <!--===============================================================================================--> \
                <script src="/static/vendor/countdowntime/countdowntime.js"></script> \
            <!--	<script src="js/main.js"></script> --> \
            <!--===============================================================================================--> \
            </body> \
            </html> '
    
    def generate(self, json_data):
        return self.page_template.format(json2html.convert(json = json_data))