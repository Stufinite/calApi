# 課程資料查詢API (API of Course code of Dept. and Time of Course)

此API可以直接查詢`系所的課程代碼`和`課程的上課時間`

## API usage and Results

API使用方式（下面所寫的是api的URL pattern）<br>
(Usage of API (pattern written below is URL pattern))：

1. *`/cphelper/course/CourseOfDept/?dept=<>&school=<>&grade=<Optional>`*  
  取得系所的課程代碼<br>
  (Get Course code of Dept Name.)：<br>

  Grade參數用來指定年級，如果不加則是回傳所有年級的必選修：
  - 全年級：`/cphelper/course/CourseOfDept/?dept=U56&school=NCHU`
    - Result：

    ```
    {
      "obligatory": {
        "三Ｂ": [
          "D17772",
          "D17771"
        ],
        "四Ａ": [
          "D17785",
          "D17782"
        ]
        ...
      },
      "optional": {
        "三Ｂ": [
          "D19777"
        ],
        "三Ａ": [
          "D19776"
        ]
        ...
      }
    }
    ```

  - 指定年級：`/course/CourseOfDept/?dept=U56&grade=3&school=NCHU`
    - result：

    ```
	{
	  "obligatory": {
	    "3": [
	      "3359","3360","3365","3366","3367","3368","3369","3370","3371","3372"
	    ]
	  },ional": {
	    "3": [
	      "3105","3110","3117","3185","3198","3314","3364"
	    ]
	  }
	}
    ```

2. *`/course/CourseOfTime/?day=<星期幾>&time=<第幾節課>&school=<學校名稱>&degree=<學制，可以是複數>&dept=<系所，可以是複數>`*  
查詢該時段有什麼課可以上：

  - 範例 (Example)：`/course/CourseOfTime/?day=1&time=1&school=NCHU&degree=O+U&dept=C00+U56`  
  代表同時查詢O（其他類別）的C00（全校共同）和U（學士班）的U56（資工系）該時段的課程  
  - *`degree`* 和 *`dept`* ：如果要使用複數的時候，請記得用 *`+`* 把參數隔開，然後是 *`degree`* 的第一個值對應到 *`dept`* 的第一個；以此類推。
  - result：

    ```
    ["1159", "2217", "3432", "3434", "3445", "3447", "3448", "3449", "3450", "3451", "3452", "3453", "3456", "3457", "3458", "3459", "3460", "3461"]
    ```

3. *`/course/get/Genra/?school=<學校名稱>`*  
該學校所有的系所和年級：

  - 範例 (Example)：`/course/get/Genra/?school=NUTC`  
  - result：

    ```
    {
      "其他類": {
        "語言": [
          "一１",
          "二１",
          "二２"
        ]
      },
      "通識類": {
        "通識": [
          "二２",
          "二１",
          "二５",
          "二３",
          "二４",
          "三Ｂ",
          "三Ａ",
          "三４",
          "三３",
          "三２",
          "三Ｄ",
          "三１",
          "三Ｃ",
          "三Ｆ",
          "三５"
        ]
      },
      "體育類": {
        "體育": [
          "二２",
          "二１",
          "二３",
          "二４",
          "三Ａ",
          "三１",
          "四丁",
          "四丙",
          "四己",
          "四戊",
          "四乙",
          "四甲",
          "四１",
          "五甲",
          "五乙"
        ]
      },
      "大學部": {
        "應中": [
          "一１",
          "二１",
          "三１",
          "四１"
        ],
        "休閒": [
          "一１",
          "二１",
          "三１",
          "四１"
        ],
        "美容系技優班": [
          "一１"
        ],
        "資應菁英班": [
          "一甲",
          "二甲",
          "三Ａ",
          "三甲",
          "四Ａ",
          "四甲",
          "五甲"
        ]
        ...
        ...
        ...
      }
    }
    ```

## Running & Testing

## Run

1. 第一次的時候，需要先初始化資料庫：`python migrate`
2. Execute : `python manage.py runserver`.
3. 插入mongodb以及django資料庫的範例指令：
    * `python manage.py buildCourse 學校genra.json 學校course.json 學校 第幾學年度`
    * 以中山大學為範例：`python manage.py buildCourse ../NSYSUgenra.json ../NSYSU.json NSYSU 1061`