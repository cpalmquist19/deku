*****************************************************
THIS IS A PLACEHOLDER README FILE FOR NOW
*****************************************************

D.E.K.U.
D.E.K.U. is a sophisticated web tool tailored for automating the extraction of navigational structures from web applications. Utilizing Python and Selenium, it methodically navigates web interfaces, identifies key navigational elements, and systematically extracts these details.

Features
Automated navigation and interaction with web interfaces using Selenium
Identifies and extracts key navigational elements like menus, tabs, links, etc.
Outputs structured data detailing the application's navigational hierarchy
Customizable through configuration files to handle different web apps
Built using Python for cross-platform compatibility

Getting Started
These instructions will help you set up D.E.K.U. on your local system.

Configure config.json

Usage
The main entry point is deku.py. This will run the extraction based on your config.json.

Config fields:

start_url - The initial URL to load
output_file - Path to save extracted nav data as JSON
depth - Crawling recursion depth
Additional WebDriver settings
Output is saved to the output file as JSON containing the hierarchical site navigation.

Customizing
You can customize and tweak D.E.K.U.'s extraction by:

Adding more element type identifiers
Creating customized navigation assemblers
Expanding crawling logic

See the wiki for more details.