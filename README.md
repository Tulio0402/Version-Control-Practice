# Version-Control-Practice
Assignment 2 for Software Engineering

## 關於 Expense-Tracking Tool

* 這是一個基於 Python 開發的簡單費用追蹤工具，由兩位開發者共同合作完成：
    * Member A (輸入模組)：實作費用輸入與資料儲存功能
    * Member B (視覺化模組)：實作資料讀取與類別圓餅圖生成功能
* 本專案旨在練習 Git 分支管理與團隊協作 

## 版本需求

* Python：3.x 或以上版本
* ==必要套件：matplotlib==（用於生成圖表）

## 安裝方式

* 切換至專案目錄
    ``` bash
    cd path/to/your/project
    ```
* 複製儲存庫：
    ``` bash
    git clone https://github.com/Tulio0402/Version-Control-Practice.git
    ```
* 安裝必要套件：
    ``` bash
    pip install matplotlib
    ```

## 如何使用

1. 啟動程式：在終端機執行 `Input_module.py` 以啟動主選單
2. 功能選單說明：
    * ==選項 1 (SHOW)==：列出目前所有已記錄的費用資訊
    * ==選項 2 (ADD)==：新增一筆費用。系統會引導您輸入：
        * 日期 (Date)：請使用 YYYY-MM-DD 格式
        * 類別 (Category)：費用類型（如：餐飲、交通）
        * 金額 (Amount)：正整數金額
        * 備註 (Notes)：此項為選填
    * ==選項 0 (EXIT)==：結束並退出程式
3. 視覺化圖表：每次成功新增費用後，系統會自動跳出圓餅圖視窗，根據不同類別統計金額比例

## Pie Chart Sample

![Figure_1](https://hackmd.io/_uploads/BknQTIZ7Ze.png)
