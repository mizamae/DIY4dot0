

# Nginx configuration for HomeAutomation

[Nginx][0] is an application that 

## Installation

### Quick start

To install Nginx on a Linux environment, type the following command:

    sudo apt-get install nginx

Once properly installed, it is automatically started once the system is booted. 
Nginx looks for incoming connections through the port and to the domains indicated in its configuration file. These files are usually placed in the path '/etc/nginx/sites-available/project'. A working example of this configuration file is the HomeAutomation.nginxconf file included here.

In order to activate the configuration file, the following steps are to be followed:
   1. Copy the configuration file to the path indicated
   2. Create a link of the file in the sites-enabled path from Nginx
			
		sudo ln -s /etc/nginx/sites-available/HomeAutomation.nginxconf /etc/nginx/sites-enabled  

   3. Test the configuration running
 		
		sudo nginx -t				
	
   4. If no errors are found, restart Nginx and you should be able to see the Nginx .
   
		sudo systemctl restart nginx

A more detailed but general manual about configuring Nginx can be found [here][1]	

### Detailed instructions

Take a look at the docs for more information.

[0]: https://nginx.org/en/
[1]: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
