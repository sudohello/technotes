/*
Title: Snippets
Decription: Snippets
Author: Bhaskar Mangal
Date: 15th-Mar-2018
Tags: Snippets
*/

# Snippets

## Javascript
var style = this.options.style;
var exec = style.exec;
exec.forEach(function(o,i){
	console.log(o);console.log(i);
	Object.keys(o).forEach(function(key,index) {
		console.log(o[key]);
		style.layers
		o[key].id
	});
})

// https://stackoverflow.com/questions/8312459/iterate-through-object-properties
Object.keys(obj).forEach(function(key,index) {
  // key: the name of the object key
  // index: the ordinal position of the key within the object
})

## PHP: SLIM 3
* **Get Base URL**
https://stackoverflow.com/questions/6782895/php-remove-filename-from-path
```php
  ["REQUEST_URI"]=>
  ["SCRIPT_NAME"]=>
  ["SERVER_NAME"]=>

  function getBaseUrl() {
  	$currentPath = $_SERVER['PHP_SELF'];
  	$currentPath = pathinfo($_SERVER["SCRIPT_NAME"], PATHINFO_DIRNAME);
  }

  if (isset($_SERVER['HTTP_HOST'])) {
    $http = isset($_SERVER['HTTPS']) && strtolower($_SERVER['HTTPS']) !== 'off' ? 'https' : 'http';
    $hostname = $_SERVER['HTTP_HOST'];
    $dir =  str_replace(basename($_SERVER['SCRIPT_NAME']), '', $_SERVER['SCRIPT_NAME']);

    $core = preg_split('@/@', str_replace($_SERVER['DOCUMENT_ROOT'], '', realpath(dirname(__FILE__))), NULL, PREG_SPLIT_NO_EMPTY);
    $core = $core[0];

    $tmplt = $atRoot ? ($atCore ? "%s://%s/%s/" : "%s://%s/") : ($atCore ? "%s://%s/%s/" : "%s://%s%s");
    $end = $atRoot ? ($atCore ? $core : $hostname) : ($atCore ? $core : $dir);
    $base_url = sprintf( $tmplt, $http, $hostname, $end );
}
```

* **slim-3-routing-best-practices**
- https://discourse.slimframework.com/t/slim-3-routing-best-practices-and-organization/93/4
```php
 $app = new Slim(
    "MODE" => "developement",
    "TEMPLATES.PATH' => "./templates"
);
#
$app->group('/v1', function () {
    $this->group('/auth', function () {
        $this->map(['GET', 'POST'], '/login', 'App\controllers\AuthController:login');
        $this->map(['GET', 'POST'], '/logout', 'App\controllers\AuthController:logout');
        $this->map(['GET', 'POST'], '/signup', 'App\controllers\AuthController:signup');
    });

    $this->group('/events', function () {
        $this->get('', 'App\controllers\EventController:getEvents');
        $this->post('', 'App\controllers\EventController:createEvent');

        $this->group('/{eventId}', function () {
            $this->get('', 'App\controllers\EventController:getEvent');
            $this->put('', 'App\controllers\EventController:updateEvent');
            $this->delete('', 'App\controllers\EventController:deleteEvent');            
        });
    });
});
# The use keyword enables us to access the outer variables from inside the scope of the anonymous function.
$app->get("/books", function () use ($app, $db) {
    $books = array();
    foreach ($db->books() as $book) {
        $books[]  = array(
            "id" => $book["id"],
            "title" => $book["title"],
            "author" => $book["author"],
            "summary" => $book["summary"]
        );
    }
    $app->response()->header("Content-Type", "application/json");
    echo json_encode($books);
});
```

**passing data to twig views in SLIM**
```php
$data = ['subscriber' => $subscriber];
return $this->container->view->render($response, 'subscriber.twig', $data);
```

**Javascript**
hoverPopup._content.parentNode.insertBefore((function() {
      var _line = document.createElement('div');
      _line.className = "line"; 
      return _line;
    })(), hoverPopup._content);


https://stackoverflow.com/questions/4793604/how-to-insert-an-element-after-another-element-in-javascript-without-using-a-lib