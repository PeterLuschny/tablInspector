'''
body{text-align:justify;width:640px;font-size:12pt;margin:auto;background-color:#E5E7E9;}
.ccl,.ccl pre{color:black;font-size:11pt;}
p.banner{padding:4px;letter-spacing:4px;text-transform:capitalize;font-weight:bold;color:yellow;background-color:#CCF;text-align:center;font-family:Verdana,'Courier New',Monospace}
.ccl pre{margin:0;line-height:1.428571429}
.ccl .rem{color:maroon}
.ccl .kwd{color:#104E8B}
.ccl .str{color:#A31515}
.ccl .op{color:#0000C0}
.ccl .preproc{color:#C63}
.ccl .asp{background-color:#FF0}
.ccl .html{color:#800000}
.ccl .attr{color:#F00}
.ccl .alt{background-color:#F4F4F4;width:100%;margin:0;line-height:1.428571429}
.ccl .lnum{color:#606060}
p{line-height:1.428571429}
.sage{color:blue;font-family:Arial, Helvetica, sans-serif;}
h1{font-family:'Droid Serif',serif;font-stretch:expanded;margin:16px 0;line-height:1.428571429;position:relative;font-size:24pt;font-weight:700;color:#D37E0C}
h2{margin:16px 0;text-transform:uppercase;letter-spacing:1px;line-height:1.428571429;position:relative;font-size:14pt;font-weight:600;color:#D37E0C}
h3{font-size:12pt;line-height:1.428571429;color:#A25000;font-weight:400}
a:link,a:visited{color:blue;text-decoration:underline}
a:hover{color:white;background-color:#D37E0C;text-decoration:none}
.q,.qa,.qb,.qc{float:left;display:block;padding:10px;border-radius:4px;margin-left:6px;font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
.qa{color:yellow;background-color:#5E7AFF;font-size:12pt;}
.qb{color:blue;background-color:lightgray;font-size:12pt;}
.qc{color:blue;background-color:lightgray;font-size:10pt;font-weight:bold}
.qa:hover,.qb:hover,.qc:hover{color:white;background-color:#D37E0C;}
.qa>a{color:#FFE793;}


<!DOCTYPE html>
<html lang='en'>
<head>
    <title>TablInspector</title>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width'>
    <link rel='stylesheet' type='text/css' href='CodeCruiser.css'>
    <script src='https://sagecell.sagemath.org/static/embedded_sagecell.js'></script>
    <script>$(function () { sagecell.makeSagecell({ 
        inputLocation: 'div.compute', evalButtonText: 'Evaluate' }); });
    </script>
</head>

<body>

<h1>The Interactive Tabl Inspector</h1>
<h4>Based on the project <a href="https://github.com/PeterLuschny/tablInspector">tablInspector</a> on GitHub.</h4> 

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>This is the list of available tables:</h4>

    <div class="compute" id="sagecell3" style="font-size: large;"><script type="text/x-sage">
load('https://raw.githubusercontent.com/PeterLuschny/tablInspector/refs/heads/main/src/Tables.py')
for t in TablesDict.keys(): print(t)
    </script></div>

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>This is the list of available traits:</h4>

    <div class="compute" id="sagecell3" style="font-size: large;"><script type="text/x-sage">
load('https://raw.githubusercontent.com/PeterLuschny/tablInspector/refs/heads/main/src/Tables.py')
for t in TraitsDict.keys(): print(t)
    </script></div>

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>By combining a table with a trait, you get more than 8000 ways to query the characteristics of tables. Below is an example.</h4>

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>What are the row sums of the inverse Schroeder triangle?</h4>

    <div class="compute" id="sagecell1" style="font-size: large;"><script type="text/x-sage">
load('https://raw.githubusercontent.com/PeterLuschny/tablInspector/refs/heads/main/src/Tables.py')
ILookUp("SchroederInv", "TablSum")
    </script></div>

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>Note that the cells are editable. You can insert all the table and trait names listed above. For instance try the above ILookUp function also with "Schroeder", "SchroederL", and "SchroederP".</h4> 

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />
<h4>Plot the first 8 row polynomials of the inverse Schroeder triangle.</h4>

    <div class="compute" id="sagecell2" style="font-size: large;"><script type="text/x-sage">
load('https://raw.githubusercontent.com/PeterLuschny/tablInspector/refs/heads/main/src/Tables.py')
TablPlot("SchroederInv", 8)
    </script></div>

<hr style='margin-top:16px;color:maroon;border-style:solid;height:2px;background-color:maroon;' />

</body></html>
'''