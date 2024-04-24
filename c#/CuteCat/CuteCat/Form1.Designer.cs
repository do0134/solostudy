namespace CuteCat
{
    partial class Form1
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
            components = new System.ComponentModel.Container();
            CatScreen = new Label();
            PlayButton = new Button();
            FeedButton = new Button();
            Bored_Timer = new System.Windows.Forms.Timer(components);
            SuspendLayout();
            // 
            // CatScreen
            // 
            CatScreen.BorderStyle = BorderStyle.Fixed3D;
            CatScreen.Location = new Point(33, 33);
            CatScreen.Name = "CatScreen";
            CatScreen.Size = new Size(736, 40);
            CatScreen.TabIndex = 0;
            CatScreen.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // PlayButton
            // 
            PlayButton.Location = new Point(33, 89);
            PlayButton.Name = "PlayButton";
            PlayButton.Size = new Size(146, 54);
            PlayButton.TabIndex = 1;
            PlayButton.Text = "Play";
            PlayButton.UseVisualStyleBackColor = true;
            PlayButton.Click += Play_Click;
            // 
            // FeedButton
            // 
            FeedButton.Location = new Point(311, 89);
            FeedButton.Name = "FeedButton";
            FeedButton.Size = new Size(146, 54);
            FeedButton.TabIndex = 2;
            FeedButton.Text = "Feed";
            FeedButton.UseVisualStyleBackColor = true;
            FeedButton.Click += Feed_Click;
            // 
            // Bored_Timer
            // 
            Bored_Timer.Enabled = true;
            Bored_Timer.Interval = 5000;
            Bored_Timer.Tick += Cat_GetBoard;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(FeedButton);
            Controls.Add(PlayButton);
            Controls.Add(CatScreen);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Label CatScreen;
        private Button PlayButton;
        private Button FeedButton;
        private System.Windows.Forms.Timer Bored_Timer;
    }
}
