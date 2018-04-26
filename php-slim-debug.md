object(Slim\Container)#2 (7) {
  ["defaultSettings":"Slim\Container":private]=>
  array(7) {
    ["httpVersion"]=>
    string(3) "1.1"
    ["responseChunkSize"]=>
    int(4096)
    ["outputBuffering"]=>
    string(6) "append"
    ["determineRouteBeforeAppMiddleware"]=>
    bool(false)
    ["displayErrorDetails"]=>
    bool(false)
    ["addContentLengthHeader"]=>
    bool(true)
    ["routerCacheFile"]=>
    bool(false)
  }
  ["values":"Pimple\Container":private]=>
  array(13) {
    ["templates"]=>
    string(46) "/home/bhaskar/public_html/smartcity/maps/views"
    ["settings"]=>
    object(Slim\Collection)#21 (1) {
      ["data":protected]=>
      array(7) {
        ["httpVersion"]=>
        string(3) "1.1"
        ["responseChunkSize"]=>
        int(4096)
        ["outputBuffering"]=>
        string(6) "append"
        ["determineRouteBeforeAppMiddleware"]=>
        bool(false)
        ["displayErrorDetails"]=>
        bool(false)
        ["addContentLengthHeader"]=>
        bool(true)
        ["routerCacheFile"]=>
        bool(false)
      }
    }
    ["environment"]=>
    object(Slim\Http\Environment)#27 (1) {
      ["data":protected]=>
      array(35) {
        ["REDIRECT_STATUS"]=>
        string(3) "200"
        ["HTTP_HOST"]=>
        string(9) "localhost"
        ["HTTP_CONNECTION"]=>
        string(10) "keep-alive"
        ["HTTP_PRAGMA"]=>
        string(8) "no-cache"
        ["HTTP_CACHE_CONTROL"]=>
        string(8) "no-cache"
        ["HTTP_UPGRADE_INSECURE_REQUESTS"]=>
        string(1) "1"
        ["HTTP_USER_AGENT"]=>
        string(105) "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        ["HTTP_ACCEPT"]=>
        string(85) "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        ["HTTP_ACCEPT_ENCODING"]=>
        string(17) "gzip, deflate, br"
        ["HTTP_ACCEPT_LANGUAGE"]=>
        string(26) "en-GB,en-US;q=0.9,en;q=0.8"
        ["PATH"]=>
        string(60) "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ["SERVER_SIGNATURE"]=>
        string(70) "<address>Apache/2.4.18 (Ubuntu) Server at localhost Port 80</address>
"
        ["SERVER_SOFTWARE"]=>
        string(22) "Apache/2.4.18 (Ubuntu)"
        ["SERVER_NAME"]=>
        string(9) "localhost"
        ["SERVER_ADDR"]=>
        string(3) "::1"
        ["SERVER_PORT"]=>
        string(2) "80"
        ["REMOTE_ADDR"]=>
        string(3) "::1"
        ["DOCUMENT_ROOT"]=>
        string(13) "/var/www/html"
        ["REQUEST_SCHEME"]=>
        string(4) "http"
        ["CONTEXT_PREFIX"]=>
        string(9) "/~bhaskar"
        ["CONTEXT_DOCUMENT_ROOT"]=>
        string(25) "/home/bhaskar/public_html"
        ["SERVER_ADMIN"]=>
        string(19) "webmaster@localhost"
        ["SCRIPT_FILENAME"]=>
        string(45) "/home/bhaskar/public_html/smartcity/index.php"
        ["REMOTE_PORT"]=>
        string(5) "54510"
        ["REDIRECT_URL"]=>
        string(34) "/~bhaskar/smartcity/infrastructure"
        ["REDIRECT_QUERY_STRING"]=>
        string(17) "q=tirupat,ward:10"
        ["GATEWAY_INTERFACE"]=>
        string(7) "CGI/1.1"
        ["SERVER_PROTOCOL"]=>
        string(8) "HTTP/1.1"
        ["REQUEST_METHOD"]=>
        string(3) "GET"
        ["QUERY_STRING"]=>
        string(17) "q=tirupat,ward:10"
        ["REQUEST_URI"]=>
        string(52) "/~bhaskar/smartcity/infrastructure?q=tirupat,ward:10"
        ["SCRIPT_NAME"]=>
        string(29) "/~bhaskar/smartcity/index.php"
        ["PHP_SELF"]=>
        string(29) "/~bhaskar/smartcity/index.php"
        ["REQUEST_TIME_FLOAT"]=>
        float(1524131359.274)
        ["REQUEST_TIME"]=>
        int(1524131359)
      }
    }
    ["request"]=>
    object(Slim\Http\Request)#33 (15) {
      ["method":protected]=>
      string(3) "GET"
      ["originalMethod":protected]=>
      string(3) "GET"
      ["uri":protected]=>
      object(Slim\Http\Uri)#31 (9) {
        ["scheme":protected]=>
        string(4) "http"
        ["user":protected]=>
        string(0) ""
        ["password":protected]=>
        string(0) ""
        ["host":protected]=>
        string(9) "localhost"
        ["port":protected]=>
        int(80)
        ["basePath":protected]=>
        string(19) "/~bhaskar/smartcity"
        ["path":protected]=>
        string(14) "infrastructure"
        ["query":protected]=>
        string(17) "q=tirupat,ward:10"
        ["fragment":protected]=>
        string(0) ""
      }
      ["requestTarget":protected]=>
      NULL
      ["queryParams":protected]=>
      NULL
      ["cookies":protected]=>
      array(0) {
      }
      ["serverParams":protected]=>
      array(35) {
        ["REDIRECT_STATUS"]=>
        string(3) "200"
        ["HTTP_HOST"]=>
        string(9) "localhost"
        ["HTTP_CONNECTION"]=>
        string(10) "keep-alive"
        ["HTTP_PRAGMA"]=>
        string(8) "no-cache"
        ["HTTP_CACHE_CONTROL"]=>
        string(8) "no-cache"
        ["HTTP_UPGRADE_INSECURE_REQUESTS"]=>
        string(1) "1"
        ["HTTP_USER_AGENT"]=>
        string(105) "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        ["HTTP_ACCEPT"]=>
        string(85) "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        ["HTTP_ACCEPT_ENCODING"]=>
        string(17) "gzip, deflate, br"
        ["HTTP_ACCEPT_LANGUAGE"]=>
        string(26) "en-GB,en-US;q=0.9,en;q=0.8"
        ["PATH"]=>
        string(60) "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ["SERVER_SIGNATURE"]=>
        string(70) "<address>Apache/2.4.18 (Ubuntu) Server at localhost Port 80</address>
"
        ["SERVER_SOFTWARE"]=>
        string(22) "Apache/2.4.18 (Ubuntu)"
        ["SERVER_NAME"]=>
        string(9) "localhost"
        ["SERVER_ADDR"]=>
        string(3) "::1"
        ["SERVER_PORT"]=>
        string(2) "80"
        ["REMOTE_ADDR"]=>
        string(3) "::1"
        ["DOCUMENT_ROOT"]=>
        string(13) "/var/www/html"
        ["REQUEST_SCHEME"]=>
        string(4) "http"
        ["CONTEXT_PREFIX"]=>
        string(9) "/~bhaskar"
        ["CONTEXT_DOCUMENT_ROOT"]=>
        string(25) "/home/bhaskar/public_html"
        ["SERVER_ADMIN"]=>
        string(19) "webmaster@localhost"
        ["SCRIPT_FILENAME"]=>
        string(45) "/home/bhaskar/public_html/smartcity/index.php"
        ["REMOTE_PORT"]=>
        string(5) "54510"
        ["REDIRECT_URL"]=>
        string(34) "/~bhaskar/smartcity/infrastructure"
        ["REDIRECT_QUERY_STRING"]=>
        string(17) "q=tirupat,ward:10"
        ["GATEWAY_INTERFACE"]=>
        string(7) "CGI/1.1"
        ["SERVER_PROTOCOL"]=>
        string(8) "HTTP/1.1"
        ["REQUEST_METHOD"]=>
        string(3) "GET"
        ["QUERY_STRING"]=>
        string(17) "q=tirupat,ward:10"
        ["REQUEST_URI"]=>
        string(52) "/~bhaskar/smartcity/infrastructure?q=tirupat,ward:10"
        ["SCRIPT_NAME"]=>
        string(29) "/~bhaskar/smartcity/index.php"
        ["PHP_SELF"]=>
        string(29) "/~bhaskar/smartcity/index.php"
        ["REQUEST_TIME_FLOAT"]=>
        float(1524131359.274)
        ["REQUEST_TIME"]=>
        int(1524131359)
      }
      ["attributes":protected]=>
      object(Slim\Collection)#34 (1) {
        ["data":protected]=>
        array(0) {
        }
      }
      ["bodyParsed":protected]=>
      bool(false)
      ["bodyParsers":protected]=>
      array(4) {
        ["application/json"]=>
        object(Closure)#36 (2) {
          ["this"]=>
          *RECURSION*
          ["parameter"]=>
          array(1) {
            ["$input"]=>
            string(10) "<required>"
          }
        }
        ["application/xml"]=>
        object(Closure)#37 (2) {
          ["this"]=>
          *RECURSION*
          ["parameter"]=>
          array(1) {
            ["$input"]=>
            string(10) "<required>"
          }
        }
        ["text/xml"]=>
        object(Closure)#38 (2) {
          ["this"]=>
          *RECURSION*
          ["parameter"]=>
          array(1) {
            ["$input"]=>
            string(10) "<required>"
          }
        }
        ["application/x-www-form-urlencoded"]=>
        object(Closure)#39 (2) {
          ["this"]=>
          *RECURSION*
          ["parameter"]=>
          array(1) {
            ["$input"]=>
            string(10) "<required>"
          }
        }
      }
      ["uploadedFiles":protected]=>
      array(0) {
      }
      ["validMethods":protected]=>
      array(9) {
        ["CONNECT"]=>
        int(1)
        ["DELETE"]=>
        int(1)
        ["GET"]=>
        int(1)
        ["HEAD"]=>
        int(1)
        ["OPTIONS"]=>
        int(1)
        ["PATCH"]=>
        int(1)
        ["POST"]=>
        int(1)
        ["PUT"]=>
        int(1)
        ["TRACE"]=>
        int(1)
      }
      ["protocolVersion":protected]=>
      string(3) "1.1"
      ["headers":protected]=>
      object(Slim\Http\Headers)#32 (1) {
        ["data":protected]=>
        array(9) {
          ["host"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(9) "localhost"
            }
            ["originalKey"]=>
            string(4) "Host"
          }
          ["connection"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(10) "keep-alive"
            }
            ["originalKey"]=>
            string(15) "HTTP_CONNECTION"
          }
          ["pragma"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(8) "no-cache"
            }
            ["originalKey"]=>
            string(11) "HTTP_PRAGMA"
          }
          ["cache-control"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(8) "no-cache"
            }
            ["originalKey"]=>
            string(18) "HTTP_CACHE_CONTROL"
          }
          ["upgrade-insecure-requests"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(1) "1"
            }
            ["originalKey"]=>
            string(30) "HTTP_UPGRADE_INSECURE_REQUESTS"
          }
          ["user-agent"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(105) "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }
            ["originalKey"]=>
            string(15) "HTTP_USER_AGENT"
          }
          ["accept"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(85) "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
            }
            ["originalKey"]=>
            string(11) "HTTP_ACCEPT"
          }
          ["accept-encoding"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(17) "gzip, deflate, br"
            }
            ["originalKey"]=>
            string(20) "HTTP_ACCEPT_ENCODING"
          }
          ["accept-language"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(26) "en-GB,en-US;q=0.9,en;q=0.8"
            }
            ["originalKey"]=>
            string(20) "HTTP_ACCEPT_LANGUAGE"
          }
        }
      }
      ["body":protected]=>
      object(Slim\Http\RequestBody)#19 (7) {
        ["stream":protected]=>
        resource(5) of type (stream)
        ["meta":protected]=>
        NULL
        ["readable":protected]=>
        NULL
        ["writable":protected]=>
        NULL
        ["seekable":protected]=>
        NULL
        ["size":protected]=>
        NULL
        ["isPipe":protected]=>
        NULL
      }
    }
    ["response"]=>
    object(Slim\Http\Response)#29 (5) {
      ["status":protected]=>
      int(200)
      ["reasonPhrase":protected]=>
      string(0) ""
      ["protocolVersion":protected]=>
      string(3) "1.1"
      ["headers":protected]=>
      object(Slim\Http\Headers)#30 (1) {
        ["data":protected]=>
        array(1) {
          ["content-type"]=>
          array(2) {
            ["value"]=>
            array(1) {
              [0]=>
              string(24) "text/html; charset=UTF-8"
            }
            ["originalKey"]=>
            string(12) "Content-Type"
          }
        }
      }
      ["body":protected]=>
      object(Slim\Http\Body)#28 (7) {
        ["stream":protected]=>
        resource(3) of type (stream)
        ["meta":protected]=>
        NULL
        ["readable":protected]=>
        NULL
        ["writable":protected]=>
        NULL
        ["seekable":protected]=>
        NULL
        ["size":protected]=>
        NULL
        ["isPipe":protected]=>
        NULL
      }
    }
    ["router"]=>
    object(Slim\Router)#22 (8) {
      ["container":protected]=>
      *RECURSION*
      ["routeParser":protected]=>
      object(FastRoute\RouteParser\Std)#23 (0) {
      }
      ["basePath":protected]=>
      string(19) "/~bhaskar/smartcity"
      ["cacheFile":protected]=>
      bool(false)
      ["routes":protected]=>
      array(2) {
        ["route0"]=>
        object(Slim\Route)#24 (13) {
          ["methods":protected]=>
          array(1) {
            [0]=>
            string(3) "GET"
          }
          ["identifier":protected]=>
          string(6) "route0"
          ["name":protected]=>
          NULL
          ["groups":protected]=>
          array(0) {
          }
          ["finalized":"Slim\Route":private]=>
          bool(false)
          ["outputBuffering":protected]=>
          string(6) "append"
          ["arguments":protected]=>
          array(0) {
          }
          ["callable":protected]=>
          object(Closure)#20 (2) {
            ["this"]=>
            *RECURSION*
            ["parameter"]=>
            array(3) {
              ["$req"]=>
              string(10) "<required>"
              ["$res"]=>
              string(10) "<required>"
              ["$arg"]=>
              string(10) "<required>"
            }
          }
          ["container":protected]=>
          *RECURSION*
          ["middleware":protected]=>
          array(0) {
          }
          ["pattern":protected]=>
          string(1) "/"
          ["tip":protected]=>
          NULL
          ["middlewareLock":protected]=>
          bool(false)
        }
        ["route1"]=>
        object(Slim\Route)#26 (13) {
          ["methods":protected]=>
          array(1) {
            [0]=>
            string(3) "GET"
          }
          ["identifier":protected]=>
          string(6) "route1"
          ["name":protected]=>
          NULL
          ["groups":protected]=>
          array(0) {
          }
          ["finalized":"Slim\Route":private]=>
          bool(true)
          ["outputBuffering":protected]=>
          string(6) "append"
          ["arguments":protected]=>
          array(1) {
            ["id"]=>
            string(14) "infrastructure"
          }
          ["callable":protected]=>
          object(Closure)#25 (2) {
            ["this"]=>
            *RECURSION*
            ["parameter"]=>
            array(3) {
              ["$req"]=>
              string(10) "<required>"
              ["$res"]=>
              string(10) "<required>"
              ["$arg"]=>
              string(10) "<required>"
            }
          }
          ["container":protected]=>
          *RECURSION*
          ["middleware":protected]=>
          array(0) {
          }
          ["pattern":protected]=>
          string(5) "/{id}"
          ["tip":protected]=>
          *RECURSION*
          ["middlewareLock":protected]=>
          bool(true)
        }
      }
      ["routeCounter":protected]=>
      int(2)
      ["routeGroups":protected]=>
      array(0) {
      }
      ["dispatcher":protected]=>
      object(FastRoute\Dispatcher\GroupCountBased)#44 (2) {
        ["staticRouteMap":protected]=>
        array(1) {
          ["GET"]=>
          array(1) {
            ["/"]=>
            string(6) "route0"
          }
        }
        ["variableRouteData":protected]=>
        array(1) {
          ["GET"]=>
          array(1) {
            [0]=>
            array(2) {
              ["regex"]=>
              string(16) "~^(?|/([^/]+))$~"
              ["routeMap"]=>
              array(1) {
                [2]=>
                array(2) {
                  [0]=>
                  string(6) "route1"
                  [1]=>
                  array(1) {
                    ["id"]=>
                    string(2) "id"
                  }
                }
              }
            }
          }
        }
      }
    }
    ["foundHandler"]=>
    object(Slim\Handlers\Strategies\RequestResponse)#42 (0) {
    }
    ["phpErrorHandler"]=>
    object(Closure)#13 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["errorHandler"]=>
    object(Closure)#14 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["notFoundHandler"]=>
    object(Closure)#15 (1) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
    }
    ["notAllowedHandler"]=>
    object(Closure)#16 (1) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
    }
    ["callableResolver"]=>
    object(Slim\CallableResolver)#35 (1) {
      ["container":"Slim\CallableResolver":private]=>
      *RECURSION*
    }
    ["view"]=>
    object(Closure)#18 (1) {
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
  }
  ["factories":"Pimple\Container":private]=>
  object(SplObjectStorage)#4 (1) {
    ["storage":"SplObjectStorage":private]=>
    array(0) {
    }
  }
  ["protected":"Pimple\Container":private]=>
  object(SplObjectStorage)#5 (1) {
    ["storage":"SplObjectStorage":private]=>
    array(0) {
    }
  }
  ["frozen":"Pimple\Container":private]=>
  array(7) {
    ["settings"]=>
    bool(true)
    ["router"]=>
    bool(true)
    ["response"]=>
    bool(true)
    ["environment"]=>
    bool(true)
    ["request"]=>
    bool(true)
    ["callableResolver"]=>
    bool(true)
    ["foundHandler"]=>
    bool(true)
  }
  ["raw":"Pimple\Container":private]=>
  array(7) {
    ["settings"]=>
    object(Closure)#6 (2) {
      ["static"]=>
      array(2) {
        ["userSettings"]=>
        array(0) {
        }
        ["defaultSettings"]=>
        array(7) {
          ["httpVersion"]=>
          string(3) "1.1"
          ["responseChunkSize"]=>
          int(4096)
          ["outputBuffering"]=>
          string(6) "append"
          ["determineRouteBeforeAppMiddleware"]=>
          bool(false)
          ["displayErrorDetails"]=>
          bool(false)
          ["addContentLengthHeader"]=>
          bool(true)
          ["routerCacheFile"]=>
          bool(false)
        }
      }
      ["this"]=>
      *RECURSION*
    }
    ["router"]=>
    object(Closure)#11 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["response"]=>
    object(Closure)#10 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["environment"]=>
    object(Closure)#8 (1) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
    }
    ["request"]=>
    object(Closure)#9 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["callableResolver"]=>
    object(Closure)#17 (2) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
      ["parameter"]=>
      array(1) {
        ["$container"]=>
        string(10) "<required>"
      }
    }
    ["foundHandler"]=>
    object(Closure)#12 (1) {
      ["this"]=>
      object(Slim\DefaultServicesProvider)#7 (0) {
      }
    }
  }
  ["keys":"Pimple\Container":private]=>
  array(13) {
    ["templates"]=>
    bool(true)
    ["settings"]=>
    bool(true)
    ["environment"]=>
    bool(true)
    ["request"]=>
    bool(true)
    ["response"]=>
    bool(true)
    ["router"]=>
    bool(true)
    ["foundHandler"]=>
    bool(true)
    ["phpErrorHandler"]=>
    bool(true)
    ["errorHandler"]=>
    bool(true)
    ["notFoundHandler"]=>
    bool(true)
    ["notAllowedHandler"]=>
    bool(true)
    ["callableResolver"]=>
    bool(true)
    ["view"]=>
    bool(true)
  }
}
