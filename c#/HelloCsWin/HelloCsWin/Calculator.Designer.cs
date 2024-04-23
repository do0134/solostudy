namespace HelloCsWin
{
    partial class Calculator
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            NumButton1 = new Button();
            NumButton2 = new Button();
            NumScreen = new Label();
            NumButton3 = new Button();
            PlusBotton = new Button();
            Result_Button = new Button();
            NumButton4 = new Button();
            NumButton5 = new Button();
            NumButton6 = new Button();
            NumButton7 = new Button();
            NumButton8 = new Button();
            NumButton9 = new Button();
            NumButton10 = new Button();
            SubButton = new Button();
            SuspendLayout();
            // 
            // NumButton1
            // 
            NumButton1.Location = new Point(16, 173);
            NumButton1.Name = "NumButton1";
            NumButton1.Size = new Size(50, 50);
            NumButton1.TabIndex = 0;
            NumButton1.Text = "1";
            NumButton1.UseVisualStyleBackColor = true;
            NumButton1.Click += NumButton_Click;
            // 
            // NumButton2
            // 
            NumButton2.Location = new Point(88, 173);
            NumButton2.Name = "NumButton2";
            NumButton2.Size = new Size(50, 50);
            NumButton2.TabIndex = 1;
            NumButton2.Text = "2";
            NumButton2.UseVisualStyleBackColor = true;
            NumButton2.Click += NumButton_Click;
            // 
            // NumScreen
            // 
            NumScreen.BorderStyle = BorderStyle.Fixed3D;
            NumScreen.Font = new Font("맑은 고딕", 12F, FontStyle.Regular, GraphicsUnit.Point, 129);
            NumScreen.Location = new Point(16, 61);
            NumScreen.Name = "NumScreen";
            NumScreen.Size = new Size(280, 30);
            NumScreen.TabIndex = 3;
            NumScreen.Text = "0";
            NumScreen.TextAlign = ContentAlignment.MiddleRight;
            // 
            // NumButton3
            // 
            NumButton3.Location = new Point(159, 173);
            NumButton3.Name = "NumButton3";
            NumButton3.Size = new Size(50, 50);
            NumButton3.TabIndex = 4;
            NumButton3.Text = "3";
            NumButton3.UseVisualStyleBackColor = true;
            NumButton3.Click += NumButton_Click;
            // 
            // PlusBotton
            // 
            PlusBotton.Location = new Point(233, 173);
            PlusBotton.Name = "PlusBotton";
            PlusBotton.Size = new Size(50, 50);
            PlusBotton.TabIndex = 5;
            PlusBotton.Text = "+";
            PlusBotton.UseVisualStyleBackColor = true;
            PlusBotton.Click += Calc;
            // 
            // Result_Button
            // 
            Result_Button.Location = new Point(233, 388);
            Result_Button.Name = "Result_Button";
            Result_Button.Size = new Size(50, 50);
            Result_Button.TabIndex = 6;
            Result_Button.Text = "=";
            Result_Button.UseVisualStyleBackColor = true;
            Result_Button.Click += Result_Button_Click;
            // 
            // NumButton4
            // 
            NumButton4.Location = new Point(16, 243);
            NumButton4.Name = "NumButton4";
            NumButton4.Size = new Size(50, 50);
            NumButton4.TabIndex = 7;
            NumButton4.Text = "4";
            NumButton4.UseVisualStyleBackColor = true;
            NumButton4.Click += NumButton_Click;
            // 
            // NumButton5
            // 
            NumButton5.Location = new Point(88, 243);
            NumButton5.Name = "NumButton5";
            NumButton5.Size = new Size(50, 50);
            NumButton5.TabIndex = 8;
            NumButton5.Text = "5";
            NumButton5.UseVisualStyleBackColor = true;
            NumButton5.Click += NumButton_Click;
            // 
            // NumButton6
            // 
            NumButton6.Location = new Point(159, 243);
            NumButton6.Name = "NumButton6";
            NumButton6.Size = new Size(50, 50);
            NumButton6.TabIndex = 9;
            NumButton6.Text = "6";
            NumButton6.UseVisualStyleBackColor = true;
            NumButton6.Click += NumButton_Click;
            // 
            // NumButton7
            // 
            NumButton7.Location = new Point(16, 318);
            NumButton7.Name = "NumButton7";
            NumButton7.Size = new Size(50, 50);
            NumButton7.TabIndex = 10;
            NumButton7.Text = "7";
            NumButton7.UseVisualStyleBackColor = true;
            NumButton7.Click += NumButton_Click;
            // 
            // NumButton8
            // 
            NumButton8.Location = new Point(88, 318);
            NumButton8.Name = "NumButton8";
            NumButton8.Size = new Size(50, 50);
            NumButton8.TabIndex = 11;
            NumButton8.Text = "8";
            NumButton8.UseVisualStyleBackColor = true;
            NumButton8.Click += NumButton_Click;
            // 
            // NumButton9
            // 
            NumButton9.Location = new Point(159, 318);
            NumButton9.Name = "NumButton9";
            NumButton9.Size = new Size(50, 50);
            NumButton9.TabIndex = 12;
            NumButton9.Text = "9";
            NumButton9.UseVisualStyleBackColor = true;
            NumButton9.MouseCaptureChanged += NumButton_Click;
            // 
            // NumButton10
            // 
            NumButton10.Location = new Point(88, 388);
            NumButton10.Name = "NumButton10";
            NumButton10.Size = new Size(50, 50);
            NumButton10.TabIndex = 13;
            NumButton10.Text = "0";
            NumButton10.UseVisualStyleBackColor = true;
            NumButton10.Click += NumButton_Click;
            // 
            // SubButton
            // 
            SubButton.Location = new Point(233, 243);
            SubButton.Name = "SubButton";
            SubButton.Size = new Size(50, 50);
            SubButton.TabIndex = 14;
            SubButton.Text = "-";
            SubButton.UseVisualStyleBackColor = true;
            SubButton.Click += Calc;
            // 
            // Calculator
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(308, 450);
            Controls.Add(SubButton);
            Controls.Add(NumButton10);
            Controls.Add(NumButton9);
            Controls.Add(NumButton8);
            Controls.Add(NumButton7);
            Controls.Add(NumButton6);
            Controls.Add(NumButton5);
            Controls.Add(NumButton4);
            Controls.Add(Result_Button);
            Controls.Add(PlusBotton);
            Controls.Add(NumButton3);
            Controls.Add(NumScreen);
            Controls.Add(NumButton2);
            Controls.Add(NumButton1);
            Name = "Calculator";
            Text = "Form1";
            Load += Calculator_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button NumButton1;
        private Button NumButton2;
        private Label NumScreen;
        private Button NumButton3;
        private Button PlusBotton;
        private Button Result_Button;
        private Button NumButton4;
        private Button NumButton5;
        private Button NumButton6;
        private Button NumButton7;
        private Button NumButton8;
        private Button NumButton9;
        private Button NumButton10;
        private Button SubButton;
    }
}
