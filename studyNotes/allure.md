## allure
#### 生成中间结果： pytest test.py --alluredir=$result_path
#### 将中间结果生成报告：allure generate -c -o $report_path $result_path
#### 报告查看： 
- 第一种方法：在ide中，report目录下的index.html用浏览器查看
- 第二种方法：用allure查看， 命令：allure open -h 127.0.0.1 -p 8765 $report_path
#### 用中间结果查看报告：
- allure serve -h 127.0.0.1 -p 8765 $result_path
  - allure serve： allure generate + allure open 
    - 即：allure serve会自动生成报告到一个tmp目录下，例如：C:\Users\tangjuan\AppData\Local\Temp\;
    - 然后展示其生成的报告
