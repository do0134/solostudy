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
            // Calculator
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(HelloLabel);
            Name = "Calculator";
            Text = "Form1";
            Load += Calculator_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label HelloLabel;
    }
}
