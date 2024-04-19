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
            HelloLabel = new Label();
            SumInput1 = new TextBox();
            SumInput2 = new TextBox();
            SumNumbers = new Button();
            SumResult = new TextBox();
            SuspendLayout();
            // 
            // HelloLabel
            // 
            HelloLabel.AutoSize = true;
            HelloLabel.Cursor = Cursors.Hand;
            HelloLabel.Font = new Font("맑은 고딕", 15F);
            HelloLabel.Location = new Point(63, 46);
            HelloLabel.Name = "HelloLabel";
            HelloLabel.Size = new Size(179, 28);
            HelloLabel.TabIndex = 0;
            HelloLabel.Text = "여기를 클릭하세요";
            HelloLabel.Click += HelloLabel_Click;
            // 
            // SumInput1
            // 
            SumInput1.Location = new Point(63, 122);
            SumInput1.Name = "SumInput1";
            SumInput1.Size = new Size(100, 23);
            SumInput1.TabIndex = 1;
            // 
            // SumInput2
            // 
            SumInput2.Location = new Point(236, 122);
            SumInput2.Name = "SumInput2";
            SumInput2.Size = new Size(100, 23);
            SumInput2.TabIndex = 2;
            // 
            // SumNumbers
            // 
            SumNumbers.Location = new Point(410, 122);
            SumNumbers.Name = "SumNumbers";
            SumNumbers.Size = new Size(75, 23);
            SumNumbers.TabIndex = 3;
            SumNumbers.Text = "=";
            SumNumbers.UseVisualStyleBackColor = true;
            SumNumbers.Click += SumNumbers_Click;
            // 
            // SumResult
            // 
            SumResult.Location = new Point(558, 122);
            SumResult.Name = "SumResult";
            SumResult.Size = new Size(100, 23);
            SumResult.TabIndex = 4;
            // 
            // Calculator
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(SumResult);
            Controls.Add(SumNumbers);
            Controls.Add(SumInput2);
            Controls.Add(SumInput1);
            Controls.Add(HelloLabel);
            Name = "Calculator";
            Text = "Form1";
            Load += Calculator_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label HelloLabel;
        private TextBox SumInput1;
        private TextBox SumInput2;
        private Button SumNumbers;
        private TextBox SumResult;
    }
}
