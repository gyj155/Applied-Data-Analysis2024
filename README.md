# 2024
Materials for Applied Data Analysis CS-401, Fall 2024

# 知识点分布

02 可视化(用库) 也可以只用pd自带绘图，如06
03 检验方法

06 07 机器学习方法：linear, logistic, forest

08 kmeans聚类，数据降维，cluster可视化
1. **Accuracy**  
   \[
   \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
   \]

2. **Precision**  
   \[
   \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
   \]

3. **Recall (Sensitivity / TPR)**  
   \[
   \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
   \]

4. **F1-score**  
   \[
   \text{F1-score} = \frac{2 \cdot (\text{Precision} \cdot \text{Recall})}{\text{Precision} + \text{Recall}}
   \]

5. **Specificity (TNR)**  
   \[
   \text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}
   \]

6. **False Positive Rate (FPR)**  
   \[
   \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
   \]

7. **False Negative Rate (FNR)**  
   \[
   \text{FNR} = \frac{\text{FN}}{\text{FN} + \text{TP}}
   \]

8. **ROC-AUC**  
   \[
   \text{AUC} = \int_{0}^{1} \text{TPR} \cdot d(\text{FPR})
   \] 