<html>
<head>
    <title>Menu d'acceuil</title>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="accueil.css">
</head>
<body>
    <div class=tr><a href="accueil.html"><h2>Menu</h2></a></div>
    <div class=center><h1>Logs</h1></div>
    <div class=center><?php

      try{
        
        $myPDO = new PDO("vos données");

        $sql = "SELECT * FROM logs";

        foreach($myPDO->query($sql)as $row){
          print "<br/>";
          print $row['date'].' - '.$row['time']. ' .......... '.$row['id'].' : '.$row['name'].' '.$row['last_name'].'<br/>';
        }
        
      
      }catch (PDOException $e){
        echo $e->getMessage();
      }
    ?></div>
</body>
</html>