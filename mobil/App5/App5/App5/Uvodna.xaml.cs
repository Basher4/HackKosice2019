using Xamarin.Forms;
using System;
using System.IO;
using Org.Json;
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
        Dictionary<string, string> info;

         public  Uvodna(string str)
		{
			InitializeComponent ();

            //info = JsonConvert.DeserializeObject<Dictionary<string, string>>(str);
            //pocet.Text = info["pos_in_queue"];
            //cas.Text = info["waiting_time"];
            //if (info["full"] == "True")
            //{
            //    objednaj.Text = "Plne";
            //    objednaj.IsEnabled = false;
           
            //}
        }
        
        async void OnSendButtonClicked(object sender, EventArgs e)
        {

            await Navigation.PushAsync(new MainPage());
        }

    }
}