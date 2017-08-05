# calApi 選課小幫手所有的api

本專案分成三種類型的api  
請去察看各自api的readme

1. [curso](curso.md)
2. [cphelper](cphelper.md)
3. [timetable](timetable.md)

## Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need `python3`

  - Linux：`sudo apt-get update; sudo apt-get install; python3 python3-dev`
  - OSX：`brew install python3`

3. service：need `mongodb`：

  - Linux：`sudo apt-get install mongodb`

## Installing

1. `pip install -r requirements.txt`

## Testing

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

## Built With

- Django==1.11.4
- djangoApiDec==1.2,
- jieba==0.38,
- pymongo==3.4.0,
- PyPrind==2.9.9,
- requests==2.12.3,
- simplejson==3.10.0,
- mongodb==3.2.11

## Contributors

- **張泰瑋** [david](https://github.com/david30907d)
- **黃川哲**

## License

This package use `MIT` License.
