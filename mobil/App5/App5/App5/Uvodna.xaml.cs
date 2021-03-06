﻿using Xamarin.Forms;
using System;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Xamarin.Forms.Xaml;
using System.Collections.Generic;

namespace App5 {  

public partial class Uvodna : ContentPage
{
    Dictionary<string, string> info;

        public Uvodna(string str)
        {
            InitializeComponent();

            info = JsonConvert.DeserializeObject<Dictionary<string, string>>(str);
            cas.Text = info["waiting"];
            if (info["full"] == "true")
            {
                objednaj.Text = "Plne";
                objednaj.IsEnabled = false;

                //}
            }
        }

        async void OnSendButtonClicked(object sender, EventArgs e)
        {

            await Navigation.PushAsync(new MainPage());
        }


        async void OnDoktorButtonClicked(object sender, EventArgs e)
        {

            await Navigation.PushAsync(new DoctorPage());
        }

    }
} 

