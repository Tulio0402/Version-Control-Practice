import matplotlib.pyplot as plt                          # 資料視覺化套件

plt.figure(figsize=(7,7))                                # 顯示圖框架大小

def pie_chart(all_expenses):
    plt.clf()                                            # 清除當前的畫布

    category_totals = {}

    for expense in all_expenses:
        category = expense[1]
        amount = expense[2]  

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    Category = list(category_totals.keys())
    Amount = list(category_totals.values())

    plt.pie(
        Amount,
        radius = 1.5,                                    # 半徑
        labels = Category,                               # 標籤
        autopct = "%2.1f%%",                             # 將數值百分比並留到小數點一位
        #explode = separeted,                            # 設定分隔的區塊位置
        pctdistance = 0.5,                               # 數字距圓心的距離
        textprops={'weight':'bold','size':16},           # 文字大小
    )

    plt.axis('equal')                                    # 使圓餅圖比例相等
    plt.title("Expenses",                                   
            fontdict={'weight':'bold','size':18},        # 設定標題及其文字大小
            y=1.05                                       # 設定標題高度
    )
    plt.legend(loc = 0)                                  # 設定圖例及其位置為最佳
    plt.draw()
    plt.pause(0.001)