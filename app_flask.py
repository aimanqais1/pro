from flask import Flask, render_template_string
import subprocess
import threading
import time

app = Flask(__name__)

# HTML template for the main page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سلسلة محاضرات معالجة الصور</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            direction: rtl;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(45deg, #2196F3, #21CBF3);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .header p {
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }
        .content {
            padding: 40px;
        }
        .app-frame {
            width: 100%;
            height: 800px;
            border: none;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .feature {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #2196F3;
        }
        .feature h3 {
            color: #2196F3;
            margin-top: 0;
        }
        .loading {
            text-align: center;
            padding: 50px;
            color: #666;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #2196F3;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🖼️ سلسلة محاضرات معالجة الصور</h1>
            <p>تطبيق تعليمي تفاعلي لتعلم أساسيات معالجة الصور الرقمية</p>
        </div>
        
        <div class="content">
            <div class="features">
                <div class="feature">
                    <h3>📚 9 محاضرات شاملة</h3>
                    <p>من أساسيات الصور الرقمية إلى التحويلات المتقدمة</p>
                </div>
                <div class="feature">
                    <h3>🔬 تجارب تفاعلية</h3>
                    <p>تطبيق عملي مباشر بدون كتابة كود</p>
                </div>
                <div class="feature">
                    <h3>📊 مقارنات مرئية</h3>
                    <p>عرض النتائج قبل وبعد المعالجة</p>
                </div>
                <div class="feature">
                    <h3>⚙️ تحكم كامل</h3>
                    <p>تعديل المعاملات والإعدادات بسهولة</p>
                </div>
            </div>
            
            <div id="loading" class="loading">
                <div class="spinner"></div>
                <p>جاري تحميل التطبيق...</p>
            </div>
            
            <iframe id="app-frame" class="app-frame" src="http://localhost:8501" style="display: none;" onload="hideLoading()"></iframe>
        </div>
    </div>

    <script>
        function hideLoading() {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('app-frame').style.display = 'block';
        }
        
        // Fallback to show iframe after 10 seconds
        setTimeout(function() {
            hideLoading();
        }, 10000);
    </script>
</body>
</html>
"""

def run_streamlit():
    """Run Streamlit app in background"""
    try:
        subprocess.Popen([
            'streamlit', 'run', 'app.py',
            '--server.port=8501',
            '--server.address=0.0.0.0',
            '--server.headless=true',
            '--server.enableCORS=false',
            '--server.enableXsrfProtection=false'
        ], cwd=r"c:\Users\MC\Desktop\project3\imm\image_processing_app")
    except Exception as e:
        print(f"Error running Streamlit: {e}")

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Start Streamlit in background thread
    streamlit_thread = threading.Thread(target=run_streamlit, daemon=True)
    streamlit_thread.start()
    
    # Wait a moment for Streamlit to start
    time.sleep(3)
    
    # Start Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)

