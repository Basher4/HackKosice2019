using Xamarin.Forms;
using System;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Xamarin.Forms.Xaml;
using System.Collections.Generic;

namespace App5
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class Uvodna : ContentPage
	{
        

         public  Uvodna(string str)
		{
			InitializeComponent ();

            Dictionary<string, string>  info = JsonConvert.DeserializeObject<Dictionary<string, string>>(str);
            //pocet.Text = info["pos_in_queue"];
            cas.Text = info["waiting"];
            if (info["full"] == "true")
            {
                objednaj.Text = "Plne";
                objednaj.IsEnabled = false;

            }
        }

        async void OnSendButtonClicked(object sender, EventArgs e)
        {

            await Navigation.PushAsync(new MainPage());
        }

    }
}