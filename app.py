import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import matplotlib.pyplot as plt

# إعداد الصفحة
st.set_page_config(
    page_title="سلسلة محاضرات معالجة الصور للمهندس ايمن قيس",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS مخصص
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E4057;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .lecture-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    .theory-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # العنوان الرئيسي
    st.markdown('<h1 class="main-header">🖼️ سلسلة محاضرات تفاعلية في معالجة الصور</h1>', unsafe_allow_html=True)
    
    # الشريط الجانبي للتنقل
    st.sidebar.title("📚 المحاضرات")
    
    lectures = {
        "الصفحة الرئيسية": "home",
        "المحاضرة 1: مدخل ومعمارية الصور الرقمية": "lecture1",
        "المحاضرة 2: أنظمة الألوان": "lecture2", 
        "المحاضرة 3: العمليات على البكسل": "lecture3",
        "المحاضرة 4: الفلاتر والالتفاف": "lecture4",
        "المحاضرة 5: إزالة الضوضاء": "lecture5",
        "المحاضرة 6: كشف الحواف": "lecture6",
        "المحاضرة 7: العمليات المورفولوجية": "lecture7",
        "المحاضرة 8: التحويلات الهندسية": "lecture8",
        "المحاضرة 9: المشروع الختامي": "lecture9"
    }
    
    selected_lecture = st.sidebar.selectbox("اختر المحاضرة:", list(lectures.keys()))
    
    # عرض المحتوى حسب المحاضرة المختارة
    if lectures[selected_lecture] == "home":
        show_home_page()
    elif lectures[selected_lecture] == "lecture1":
        show_lecture1()
    elif lectures[selected_lecture] == "lecture2":
        show_lecture2()
    elif lectures[selected_lecture] == "lecture3":
        show_lecture3()
    elif lectures[selected_lecture] == "lecture4":
        show_lecture4()
    elif lectures[selected_lecture] == "lecture5":
        show_lecture5()
    elif lectures[selected_lecture] == "lecture6":
        show_lecture6()
    elif lectures[selected_lecture] == "lecture7":
        show_lecture7()
    elif lectures[selected_lecture] == "lecture8":
        show_lecture8()
    elif lectures[selected_lecture] == "lecture9":
        show_lecture9()

def show_home_page():
    """عرض الصفحة الرئيسية"""
    st.markdown("""
    ## 🎯 أهداف السلسلة
    
    تهدف هذه السلسلة التفاعلية إلى تعليم أساسيات معالجة الصور الرقمية من خلال:
    
    - **الشرح النظري المبسط** لكل مفهوم
    - **التطبيق العملي التفاعلي** بدون كتابة كود
    - **المقارنة المباشرة** بين الصورة الأصلية والنتيجة
    - **التحكم الكامل** في المعاملات والإعدادات
    
    ## 📋 محتوى السلسلة
    """)
    
    # عرض قائمة المحاضرات
    lecture_descriptions = [
        ("المحاضرة 1", "مدخل ومعمارية الصور الرقمية", "تعرف على البكسل والأبعاد والقنوات"),
        ("المحاضرة 2", "أنظمة الألوان", "RGB, HSV, Gray وتحويل بينها"),
        ("المحاضرة 3", "العمليات على البكسل", "السطوع والتباين والعتبة"),
        ("المحاضرة 4", "الفلاتر والالتفاف", "Blur, Sharpen, Edge Detection"),
        ("المحاضرة 5", "إزالة الضوضاء", "Median, Bilateral Filtering"),
        ("المحاضرة 6", "كشف الحواف", "Sobel, Laplacian, Canny"),
        ("المحاضرة 7", "العمليات المورفولوجية", "Erosion, Dilation, Opening, Closing"),
        ("المحاضرة 8", "التحويلات الهندسية", "Rotation, Scaling, Translation"),
        ("المحاضرة 9", "المشروع الختامي", "تطبيق شامل لجميع العمليات")
    ]
    
    for i, (title, subtitle, description) in enumerate(lecture_descriptions, 1):
        with st.expander(f"{title}: {subtitle}"):
            st.write(f"📝 {description}")
    
    st.markdown("""
    ---
    ## 🚀 ابدأ الآن
    
    اختر المحاضرة الأولى من الشريط الجانبي لبدء رحلتك في تعلم معالجة الصور!
    """)

# دوال المحاضرات (سيتم تطويرها في المراحل التالية)
def show_lecture1():
    st.title("المحاضرة 1: مدخل ومعمارية الصور الرقمية")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>ما هي الصورة الرقمية؟</strong></p>
    <p>الصورة الرقمية هي مصفوفة ثنائية أو ثلاثية الأبعاد من البكسلات (Pixels). كل بكسل يحتوي على قيمة رقمية تمثل شدة الإضاءة أو اللون.</p>
    <p><strong>المكونات الأساسية:</strong></p>
    <ul>
    <li><strong>البكسل (Pixel):</strong> أصغر وحدة في الصورة</li>
    <li><strong>الأبعاد:</strong> العرض × الارتفاع × القنوات</li>
    <li><strong>العمق اللوني:</strong> عدد البتات لكل بكسل (8-bit, 16-bit, etc.)</li>
    <li><strong>القنوات (Channels):</strong> R, G, B للألوان أو قناة واحدة للرمادي</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # خيارات تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📁 تحميل صورة")
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'])
    
    with col2:
        st.subheader("🖼️ أو استخدم صورة نموذجية")
        use_sample = st.button("استخدم صورة نموذجية")
    
    # معالجة الصورة
    if uploaded_file is not None:
        # تحميل الصورة المرفوعة
        image = load_image(uploaded_file)
        process_image_info(image, "الصورة المرفوعة")
        
    elif use_sample:
        # إنشاء صورة نموذجية
        sample_image = create_sample_image()
        process_image_info(sample_image, "الصورة النموذجية")

def process_image_info(image, title):
    """معالجة وعرض معلومات الصورة"""
    st.markdown(f"### 📊 تحليل {title}")
    
    # عرض الصورة الأصلية
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("الصورة الأصلية")
        st.image(image, caption=title, use_column_width=True)
    
    with col2:
        st.subheader("معلومات الصورة")
        
        # الأبعاد
        height, width = image.shape[:2]
        channels = image.shape[2] if len(image.shape) == 3 else 1
        
        st.metric("الارتفاع (Height)", f"{height} بكسل")
        st.metric("العرض (Width)", f"{width} بكسل")
        st.metric("القنوات (Channels)", channels)
        st.metric("إجمالي البكسلات", f"{height * width:,}")
        
        # نوع البيانات
        st.write(f"**نوع البيانات:** {image.dtype}")
        st.write(f"**الحد الأدنى للقيم:** {image.min()}")
        st.write(f"**الحد الأقصى للقيم:** {image.max()}")
        st.write(f"**متوسط القيم:** {image.mean():.2f}")
    
    # عرض تفاصيل القنوات
    if len(image.shape) == 3 and image.shape[2] == 3:
        st.markdown("### 🎨 تحليل القنوات")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("القناة الحمراء (R)")
            red_channel = image[:, :, 0]
            st.image(red_channel, caption="Red Channel", use_column_width=True, clamp=True)
            st.write(f"متوسط: {red_channel.mean():.2f}")
        
        with col2:
            st.subheader("القناة الخضراء (G)")
            green_channel = image[:, :, 1]
            st.image(green_channel, caption="Green Channel", use_column_width=True, clamp=True)
            st.write(f"متوسط: {green_channel.mean():.2f}")
        
        with col3:
            st.subheader("القناة الزرقاء (B)")
            blue_channel = image[:, :, 2]
            st.image(blue_channel, caption="Blue Channel", use_column_width=True, clamp=True)
            st.write(f"متوسط: {blue_channel.mean():.2f}")
    
    # رسم بياني للتوزيع
    st.markdown("### 📈 توزيع شدة البكسلات")
    
    if len(image.shape) == 3:
        # للصور الملونة
        fig, ax = plt.subplots(figsize=(10, 4))
        colors = ['red', 'green', 'blue']
        labels = ['أحمر', 'أخضر', 'أزرق']
        
        for i, (color, label) in enumerate(zip(colors, labels)):
            hist, bins = np.histogram(image[:, :, i].flatten(), bins=50, range=(0, 255))
            ax.plot(bins[:-1], hist, color=color, label=label, alpha=0.7)
        
        ax.set_xlabel('شدة البكسل')
        ax.set_ylabel('التكرار')
        ax.set_title('توزيع شدة البكسلات لكل قناة')
        ax.legend()
        st.pyplot(fig)
    else:
        # للصور الرمادية
        fig, ax = plt.subplots(figsize=(10, 4))
        hist, bins = np.histogram(image.flatten(), bins=50, range=(0, 255))
        ax.plot(bins[:-1], hist, color='gray')
        ax.set_xlabel('شدة البكسل')
        ax.set_ylabel('التكرار')
        ax.set_title('توزيع شدة البكسلات')
        st.pyplot(fig)

def create_sample_image():
    """إنشاء صورة نموذجية للاختبار"""
    # إنشاء صورة ملونة بسيطة
    height, width = 200, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # إضافة أشكال ملونة
    # مربع أحمر
    image[50:100, 50:100] = [255, 0, 0]
    # مربع أخضر
    image[50:100, 150:200] = [0, 255, 0]
    # مربع أزرق
    image[120:170, 100:150] = [0, 0, 255]
    
    return image

def show_lecture2():
    st.title("المحاضرة 2: أنظمة الألوان")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>أنظمة الألوان (Color Spaces):</strong></p>
    <ul>
    <li><strong>RGB:</strong> أحمر، أخضر، أزرق - النظام الأكثر شيوعاً في الشاشات</li>
    <li><strong>BGR:</strong> أزرق، أخضر، أحمر - يستخدمه OpenCV افتراضياً</li>
    <li><strong>Gray:</strong> الرمادي - قناة واحدة فقط، يوفر الذاكرة ويسرع المعالجة</li>
    <li><strong>HSV:</strong> تدرج، تشبع، قيمة - مفيد لكشف الألوان وتطبيقات الرؤية الحاسوبية</li>
    </ul>
    <p><strong>متى نستخدم كل نظام؟</strong> RGB للعرض، Gray للمعالجة السريعة، HSV لكشف الألوان</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture2")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample2")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        show_color_spaces(image)
    elif use_sample:
        sample_image = create_colorful_sample_image()
        show_color_spaces(sample_image)

def show_color_spaces(image):
    """عرض تحويلات أنظمة الألوان"""
    st.markdown("### 🎨 تحويل أنظمة الألوان")
    
    # تحويل الصورة إلى تنسيق OpenCV
    if len(image.shape) == 3:
        # تحويل من RGB إلى BGR للعمل مع OpenCV
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # التحويلات المختلفة
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        
        # عرض الصور
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("الصورة الأصلية (RGB)")
            st.image(image, caption="RGB Image", use_column_width=True)
        
        with col2:
            st.subheader("الصورة الرمادية (Gray)")
            st.image(gray_image, caption="Grayscale Image", use_column_width=True, clamp=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("نظام HSV")
            # تحويل HSV للعرض
            hsv_display = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
            st.image(hsv_display, caption="HSV Image", use_column_width=True)
        
        with col4:
            st.subheader("معلومات التحويل")
            st.write("**RGB → Gray:** متوسط مرجح للقنوات الثلاث")
            st.write("**RGB → HSV:** تحويل إلى تدرج وتشبع وقيمة")
            st.write(f"**حجم RGB:** {image.shape}")
            st.write(f"**حجم Gray:** {gray_image.shape}")
            st.write(f"**حجم HSV:** {hsv_image.shape}")
    
    # تقسيم القنوات
    if len(image.shape) == 3 and image.shape[2] == 3:
        st.markdown("### 🔍 تقسيم القنوات")
        
        tab1, tab2 = st.tabs(["قنوات RGB", "قنوات HSV"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("القناة الحمراء")
                red_channel = image[:, :, 0]
                st.image(red_channel, caption="Red Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {red_channel.mean():.1f}")
                st.write(f"الانحراف المعياري: {red_channel.std():.1f}")
            
            with col2:
                st.subheader("القناة الخضراء")
                green_channel = image[:, :, 1]
                st.image(green_channel, caption="Green Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {green_channel.mean():.1f}")
                st.write(f"الانحراف المعياري: {green_channel.std():.1f}")
            
            with col3:
                st.subheader("القناة الزرقاء")
                blue_channel = image[:, :, 2]
                st.image(blue_channel, caption="Blue Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {blue_channel.mean():.1f}")
                st.write(f"الانحراف المعياري: {blue_channel.std():.1f}")
        
        with tab2:
            # تحويل إلى HSV لتقسيم القنوات
            bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("التدرج (Hue)")
                hue_channel = hsv_image[:, :, 0]
                st.image(hue_channel, caption="Hue Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {hue_channel.mean():.1f}")
            
            with col2:
                st.subheader("التشبع (Saturation)")
                sat_channel = hsv_image[:, :, 1]
                st.image(sat_channel, caption="Saturation Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {sat_channel.mean():.1f}")
            
            with col3:
                st.subheader("القيمة (Value)")
                val_channel = hsv_image[:, :, 2]
                st.image(val_channel, caption="Value Channel", use_column_width=True, clamp=True)
                st.write(f"المتوسط: {val_channel.mean():.1f}")

def create_colorful_sample_image():
    """إنشاء صورة نموذجية ملونة"""
    height, width = 200, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # إنشاء تدرجات ملونة
    for i in range(height):
        for j in range(width):
            # تدرج قوس قزح
            hue = int((j / width) * 180)
            saturation = 255
            value = 255 - int((i / height) * 100)
            
            # تحويل HSV إلى RGB
            hsv_pixel = np.uint8([[[hue, saturation, value]]])
            rgb_pixel = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2RGB)
            image[i, j] = rgb_pixel[0, 0]
    
    return image

def show_lecture3():
    st.title("المحاضرة 3: العمليات على البكسل")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>العمليات النقطية (Point Operations):</strong> تطبق على كل بكسل بشكل منفصل</p>
    <ul>
    <li><strong>السطوع (Brightness):</strong> إضافة قيمة ثابتة لكل بكسل</li>
    <li><strong>التباين (Contrast):</strong> ضرب كل بكسل في معامل</li>
    <li><strong>الصورة السالبة (Negative):</strong> عكس قيم البكسلات</li>
    <li><strong>العتبة (Thresholding):</strong> تحويل الصورة إلى ثنائية (أسود/أبيض)</li>
    </ul>
    <p><strong>الصيغة الرياضية:</strong> Output = α × Input + β</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture3")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample3")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_point_operations(image)
    elif use_sample:
        sample_image = create_sample_image()
        apply_point_operations(sample_image)

def apply_point_operations(image):
    """تطبيق العمليات النقطية"""
    st.markdown("### ⚙️ التحكم في المعاملات")
    
    # أدوات التحكم
    col1, col2 = st.columns(2)
    
    with col1:
        brightness = st.slider("السطوع (Brightness)", -100, 100, 0)
        contrast = st.slider("التباين (Contrast)", 0.1, 3.0, 1.0, 0.1)
    
    with col2:
        apply_negative = st.checkbox("تطبيق الصورة السالبة")
        threshold_value = st.slider("قيمة العتبة (Threshold)", 0, 255, 127)
    
    # تطبيق العمليات
    processed_image = image.copy().astype(np.float32)
    
    # السطوع والتباين
    processed_image = contrast * processed_image + brightness
    processed_image = np.clip(processed_image, 0, 255).astype(np.uint8)
    
    # الصورة السالبة
    if apply_negative:
        processed_image = 255 - processed_image
    
    # تحويل إلى رمادي للعتبة
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_processed = cv2.cvtColor(processed_image, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image
        gray_processed = processed_image
    
    # تطبيق العتبة
    _, threshold_image = cv2.threshold(gray_processed, threshold_value, 255, cv2.THRESH_BINARY)
    
    # تطبيق Otsu
    _, otsu_image = cv2.threshold(gray_processed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    tab1, tab2, tab3 = st.tabs(["السطوع والتباين", "الصورة السالبة", "العتبة"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("الصورة الأصلية")
            st.image(image, caption="Original", use_column_width=True)
            st.write(f"متوسط القيم: {image.mean():.1f}")
        
        with col2:
            st.subheader("بعد التعديل")
            st.image(processed_image, caption=f"Brightness: {brightness}, Contrast: {contrast}", use_column_width=True)
            st.write(f"متوسط القيم: {processed_image.mean():.1f}")
    
    with tab2:
        if apply_negative:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("قبل العكس")
                temp_image = image.copy().astype(np.float32)
                temp_image = contrast * temp_image + brightness
                temp_image = np.clip(temp_image, 0, 255).astype(np.uint8)
                st.image(temp_image, caption="Before Negative", use_column_width=True)
            
            with col2:
                st.subheader("بعد العكس")
                st.image(processed_image, caption="After Negative", use_column_width=True)
        else:
            st.info("قم بتفعيل خيار 'الصورة السالبة' لرؤية التأثير")
    
    with tab3:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("الصورة الرمادية")
            st.image(gray_processed, caption="Grayscale", use_column_width=True, clamp=True)
        
        with col2:
            st.subheader(f"عتبة يدوية ({threshold_value})")
            st.image(threshold_image, caption="Manual Threshold", use_column_width=True, clamp=True)
        
        with col3:
            st.subheader("عتبة Otsu التلقائية")
            st.image(otsu_image, caption="Otsu Threshold", use_column_width=True, clamp=True)
    
    # إحصائيات مقارنة
    st.markdown("### 📈 إحصائيات مقارنة")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    
    with stats_col1:
        st.metric("متوسط الأصلية", f"{image.mean():.1f}")
        st.metric("انحراف معياري أصلي", f"{image.std():.1f}")
    
    with stats_col2:
        st.metric("متوسط المعدلة", f"{processed_image.mean():.1f}")
        st.metric("انحراف معياري معدل", f"{processed_image.std():.1f}")
    
    with stats_col3:
        diff = processed_image.astype(np.float32) - image.astype(np.float32)
        st.metric("متوسط الفرق", f"{diff.mean():.1f}")
        st.metric("أقصى فرق", f"{np.abs(diff).max():.1f}")
    
    # رسم بياني للتوزيع
    if st.checkbox("عرض توزيع البكسلات"):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # الصورة الأصلية
        if len(image.shape) == 3:
            for i, color in enumerate(['red', 'green', 'blue']):
                hist, bins = np.histogram(image[:, :, i].flatten(), bins=50, range=(0, 255))
                ax1.plot(bins[:-1], hist, color=color, alpha=0.7)
        else:
            hist, bins = np.histogram(image.flatten(), bins=50, range=(0, 255))
            ax1.plot(bins[:-1], hist, color='gray')
        
        ax1.set_title('توزيع الصورة الأصلية')
        ax1.set_xlabel('شدة البكسل')
        ax1.set_ylabel('التكرار')
        
        # الصورة المعدلة
        if len(processed_image.shape) == 3:
            for i, color in enumerate(['red', 'green', 'blue']):
                hist, bins = np.histogram(processed_image[:, :, i].flatten(), bins=50, range=(0, 255))
                ax2.plot(bins[:-1], hist, color=color, alpha=0.7)
        else:
            hist, bins = np.histogram(processed_image.flatten(), bins=50, range=(0, 255))
            ax2.plot(bins[:-1], hist, color='gray')
        
        ax2.set_title('توزيع الصورة المعدلة')
        ax2.set_xlabel('شدة البكسل')
        ax2.set_ylabel('التكرار')
        
        plt.tight_layout()
        st.pyplot(fig)

def show_lecture4():
    st.title("المحاضرة 4: الفلاتر والالتفاف")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>الالتفاف (Convolution):</strong> عملية رياضية تطبق مرشح (Kernel) على الصورة</p>
    <ul>
    <li><strong>Kernel/Mask:</strong> مصفوفة صغيرة تحدد نوع التأثير</li>
    <li><strong>Blur:</strong> تنعيم الصورة وإزالة التفاصيل الدقيقة</li>
    <li><strong>Sharpen:</strong> تحديد الحواف وزيادة وضوح التفاصيل</li>
    <li><strong>Edge Detection:</strong> كشف الحواف والانتقالات في الصورة</li>
    </ul>
    <p><strong>التطبيقات:</strong> تحسين جودة الصور، إزالة الضوضاء، كشف الأشكال</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture4")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample4")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_filters(image)
    elif use_sample:
        sample_image = create_detailed_sample_image()
        apply_filters(sample_image)

def apply_filters(image):
    """تطبيق الفلاتر المختلفة"""
    st.markdown("### ⚙️ اختيار الفلتر")
    
    # خيارات الفلاتر
    filter_type = st.selectbox(
        "نوع الفلتر:",
        ["Blur", "Gaussian Blur", "Median Blur", "Sharpen", "Edge Detection", "Emboss", "Custom Kernel"]
    )
    
    # معاملات الفلتر
    col1, col2 = st.columns(2)
    
    with col1:
        if filter_type in ["Blur", "Gaussian Blur", "Median Blur"]:
            kernel_size = st.slider("حجم الفلتر", 3, 15, 5, step=2)
        elif filter_type == "Custom Kernel":
            st.subheader("Kernel مخصص (3x3)")
            kernel = np.zeros((3, 3))
            for i in range(3):
                cols = st.columns(3)
                for j in range(3):
                    with cols[j]:
                        kernel[i, j] = st.number_input(f"[{i},{j}]", value=0.0, format="%.2f", key=f"kernel_{i}_{j}")
    
    with col2:
        if filter_type == "Gaussian Blur":
            sigma = st.slider("Sigma", 0.1, 5.0, 1.0, 0.1)
        elif filter_type == "Edge Detection":
            edge_method = st.selectbox("طريقة كشف الحواف:", ["Sobel", "Laplacian", "Scharr"])
    
    # تطبيق الفلتر
    if len(image.shape) == 3:
        # تحويل إلى BGR للعمل مع OpenCV
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    else:
        bgr_image = image
    
    # تطبيق الفلتر المحدد
    if filter_type == "Blur":
        filtered_image = cv2.blur(bgr_image, (kernel_size, kernel_size))
    elif filter_type == "Gaussian Blur":
        filtered_image = cv2.GaussianBlur(bgr_image, (kernel_size, kernel_size), sigma)
    elif filter_type == "Median Blur":
        filtered_image = cv2.medianBlur(bgr_image, kernel_size)
    elif filter_type == "Sharpen":
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        filtered_image = cv2.filter2D(bgr_image, -1, kernel)
    elif filter_type == "Edge Detection":
        # تحويل إلى رمادي أولاً
        if len(bgr_image.shape) == 3:
            gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        else:
            gray = bgr_image
            
        if edge_method == "Sobel":
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            filtered_image = np.sqrt(sobelx**2 + sobely**2)
        elif edge_method == "Laplacian":
            filtered_image = cv2.Laplacian(gray, cv2.CV_64F)
        elif edge_method == "Scharr":
            scharrx = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
            scharry = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
            filtered_image = np.sqrt(scharrx**2 + scharry**2)
        
        # تحويل إلى uint8
        filtered_image = np.uint8(np.absolute(filtered_image))
    elif filter_type == "Emboss":
        kernel = np.array([[-2, -1,  0],
                          [-1,  1,  1],
                          [ 0,  1,  2]])
        filtered_image = cv2.filter2D(bgr_image, -1, kernel)
    elif filter_type == "Custom Kernel":
        filtered_image = cv2.filter2D(bgr_image, -1, kernel)
    
    # تحويل النتيجة للعرض
    if len(filtered_image.shape) == 3 and filtered_image.shape[2] == 3:
        display_filtered = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
    else:
        display_filtered = filtered_image
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("الصورة الأصلية")
        st.image(image, caption="Original Image", use_column_width=True)
        st.write(f"الأبعاد: {image.shape}")
        st.write(f"متوسط القيم: {image.mean():.1f}")
    
    with col2:
        st.subheader(f"بعد تطبيق {filter_type}")
        st.image(display_filtered, caption=f"Filtered Image - {filter_type}", use_column_width=True)
        st.write(f"الأبعاد: {display_filtered.shape}")
        st.write(f"متوسط القيم: {display_filtered.mean():.1f}")
    
    # عرض الفرق
    if st.checkbox("عرض الفرق بين الصور"):
        if len(image.shape) == len(display_filtered.shape):
            if len(image.shape) == 3:
                # تحويل إلى رمادي للمقارنة
                gray_original = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                if len(display_filtered.shape) == 3:
                    gray_filtered = cv2.cvtColor(display_filtered, cv2.COLOR_RGB2GRAY)
                else:
                    gray_filtered = display_filtered
            else:
                gray_original = image
                gray_filtered = display_filtered
            
            diff = np.abs(gray_original.astype(np.float32) - gray_filtered.astype(np.float32))
            st.subheader("الفرق بين الصور")
            st.image(diff, caption="Difference", use_column_width=True, clamp=True)
            st.write(f"متوسط الفرق: {diff.mean():.1f}")
            st.write(f"أقصى فرق: {diff.max():.1f}")
    
    # عرض معلومات الفلتر
    st.markdown("### 📋 معلومات الفلتر")
    
    if filter_type == "Custom Kernel":
        st.write("**الـ Kernel المستخدم:**")
        st.write(kernel)
    elif filter_type in ["Blur", "Gaussian Blur", "Median Blur"]:
        st.write(f"**حجم الفلتر:** {kernel_size}x{kernel_size}")
        if filter_type == "Gaussian Blur":
            st.write(f"**Sigma:** {sigma}")
    elif filter_type == "Sharpen":
        sharpen_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])
        st.write("**Sharpen Kernel:**")
        st.write(sharpen_kernel)
    elif filter_type == "Emboss":
        emboss_kernel = np.array([[-2, -1,  0],
                                 [-1,  1,  1],
                                 [ 0,  1,  2]])
        st.write("**Emboss Kernel:**")
        st.write(emboss_kernel)

def create_detailed_sample_image():
    """إنشاء صورة نموذجية مفصلة للفلاتر"""
    height, width = 200, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # خلفية بيضاء
    image.fill(255)
    
    # إضافة أشكال مختلفة
    # مربع أسود
    cv2.rectangle(image, (50, 50), (100, 100), (0, 0, 0), -1)
    
    # دائرة حمراء
    cv2.circle(image, (200, 75), 30, (255, 0, 0), -1)
    
    # خط أزرق
    cv2.line(image, (50, 150), (250, 150), (0, 0, 255), 3)
    
    # مثلث أخضر
    pts = np.array([[150, 120], [120, 180], [180, 180]], np.int32)
    cv2.fillPoly(image, [pts], (0, 255, 0))
    
    # إضافة ضوضاء
    noise = np.random.randint(0, 50, image.shape, dtype=np.uint8)
    image = cv2.add(image, noise)
    
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def show_lecture5():
    st.title("المحاضرة 5: إزالة الضوضاء")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>الضوضاء في الصور:</strong> بكسلات غير مرغوب فيها تؤثر على جودة الصورة</p>
    <ul>
    <li><strong>Salt & Pepper:</strong> نقاط بيضاء وسوداء عشوائية</li>
    <li><strong>Gaussian Noise:</strong> ضوضاء موزعة طبيعياً</li>
    <li><strong>Median Filter:</strong> فعال ضد Salt & Pepper</li>
    <li><strong>Bilateral Filter:</strong> يحافظ على الحواف أثناء التنعيم</li>
    </ul>
    <p><strong>الهدف:</strong> إزالة الضوضاء مع الحفاظ على التفاصيل المهمة</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture5")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample5")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_denoising(image)
    elif use_sample:
        sample_image = create_sample_image()
        apply_denoising(sample_image)

def apply_denoising(image):
    """تطبيق تقنيات إزالة الضوضاء"""
    st.markdown("### ⚙️ إعدادات إزالة الضوضاء")
    
    # خيارات إضافة الضوضاء
    col1, col2 = st.columns(2)
    
    with col1:
        add_noise = st.checkbox("إضافة ضوضاء للاختبار")
        if add_noise:
            noise_type = st.selectbox("نوع الضوضاء:", ["Salt & Pepper", "Gaussian"])
            noise_intensity = st.slider("شدة الضوضاء", 0.01, 0.3, 0.1, 0.01)
    
    with col2:
        denoising_method = st.selectbox(
            "طريقة إزالة الضوضاء:",
            ["Median Filter", "Bilateral Filter", "Gaussian Blur", "Non-local Means"]
        )
        
        if denoising_method == "Median Filter":
            kernel_size = st.slider("حجم الفلتر", 3, 15, 5, step=2)
        elif denoising_method == "Bilateral Filter":
            d = st.slider("قطر الفلتر", 5, 15, 9)
            sigma_color = st.slider("Sigma Color", 10, 150, 75)
            sigma_space = st.slider("Sigma Space", 10, 150, 75)
        elif denoising_method == "Gaussian Blur":
            kernel_size = st.slider("حجم الفلتر", 3, 15, 5, step=2)
            sigma = st.slider("Sigma", 0.1, 5.0, 1.0, 0.1)
        elif denoising_method == "Non-local Means":
            h = st.slider("Filter Strength", 3, 20, 10)
            template_window_size = st.slider("Template Window Size", 3, 11, 7, step=2)
            search_window_size = st.slider("Search Window Size", 11, 31, 21, step=2)
    
    # إضافة الضوضاء إذا طُلب ذلك
    if add_noise:
        noisy_image = add_noise_to_image(image, noise_type, noise_intensity)
        working_image = noisy_image
    else:
        working_image = image
    
    # تطبيق إزالة الضوضاء
    if len(working_image.shape) == 3:
        bgr_image = cv2.cvtColor(working_image, cv2.COLOR_RGB2BGR)
    else:
        bgr_image = working_image
    
    if denoising_method == "Median Filter":
        denoised_image = cv2.medianBlur(bgr_image, kernel_size)
    elif denoising_method == "Bilateral Filter":
        denoised_image = cv2.bilateralFilter(bgr_image, d, sigma_color, sigma_space)
    elif denoising_method == "Gaussian Blur":
        denoised_image = cv2.GaussianBlur(bgr_image, (kernel_size, kernel_size), sigma)
    elif denoising_method == "Non-local Means":
        if len(bgr_image.shape) == 3:
            denoised_image = cv2.fastNlMeansDenoisingColored(bgr_image, None, h, h, template_window_size, search_window_size)
        else:
            denoised_image = cv2.fastNlMeansDenoising(bgr_image, None, h, template_window_size, search_window_size)
    
    # تحويل للعرض
    if len(denoised_image.shape) == 3:
        display_denoised = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB)
    else:
        display_denoised = denoised_image
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    if add_noise:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("الصورة الأصلية")
            st.image(image, caption="Original", use_column_width=True)
            st.write(f"PSNR: ∞ dB")
        
        with col2:
            st.subheader("مع الضوضاء")
            st.image(working_image, caption=f"With {noise_type} Noise", use_column_width=True)
            psnr_noisy = calculate_psnr(image, working_image)
            st.write(f"PSNR: {psnr_noisy:.2f} dB")
        
        with col3:
            st.subheader("بعد إزالة الضوضاء")
            st.image(display_denoised, caption=f"Denoised - {denoising_method}", use_column_width=True)
            psnr_denoised = calculate_psnr(image, display_denoised)
            st.write(f"PSNR: {psnr_denoised:.2f} dB")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("الصورة الأصلية")
            st.image(image, caption="Original", use_column_width=True)
            st.write(f"متوسط القيم: {image.mean():.1f}")
            st.write(f"الانحراف المعياري: {image.std():.1f}")
        
        with col2:
            st.subheader("بعد إزالة الضوضاء")
            st.image(display_denoised, caption=f"Denoised - {denoising_method}", use_column_width=True)
            st.write(f"متوسط القيم: {display_denoised.mean():.1f}")
            st.write(f"الانحراف المعياري: {display_denoised.std():.1f}")
    
    # مقارنة تفصيلية
    st.markdown("### 📈 تحليل الأداء")
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.metric("تحسن الوضوح", f"{calculate_sharpness_improvement(working_image, display_denoised):.1f}%")
    
    with metrics_col2:
        st.metric("تقليل الضوضاء", f"{calculate_noise_reduction(working_image, display_denoised):.1f}%")
    
    with metrics_col3:
        if add_noise:
            st.metric("تحسن PSNR", f"{psnr_denoised - psnr_noisy:.2f} dB")
        else:
            st.metric("تنعيم الصورة", f"{working_image.std() - display_denoised.std():.1f}")

def add_noise_to_image(image, noise_type, intensity):
    """إضافة ضوضاء للصورة"""
    noisy_image = image.copy()
    
    if noise_type == "Salt & Pepper":
        # إضافة ضوضاء ملح وفلفل
        noise = np.random.random(image.shape[:2])
        noisy_image[noise < intensity/2] = 0  # فلفل (أسود)
        noisy_image[noise > 1 - intensity/2] = 255  # ملح (أبيض)
    
    elif noise_type == "Gaussian":
        # إضافة ضوضاء غاوسية
        mean = 0
        std = intensity * 255
        noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
        noisy_image = cv2.add(image, noise)
    
    return noisy_image

def calculate_psnr(original, processed):
    """حساب PSNR"""
    mse = np.mean((original.astype(np.float32) - processed.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_sharpness_improvement(original, processed):
    """حساب تحسن الوضوح"""
    # استخدام Laplacian للقياس
    if len(original.shape) == 3:
        gray_orig = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        gray_proc = cv2.cvtColor(processed, cv2.COLOR_RGB2GRAY)
    else:
        gray_orig = original
        gray_proc = processed
    
    laplacian_orig = cv2.Laplacian(gray_orig, cv2.CV_64F).var()
    laplacian_proc = cv2.Laplacian(gray_proc, cv2.CV_64F).var()
    
    if laplacian_orig == 0:
        return 0
    
    improvement = ((laplacian_proc - laplacian_orig) / laplacian_orig) * 100
    return improvement

def calculate_noise_reduction(original, processed):
    """حساب تقليل الضوضاء"""
    noise_orig = original.std()
    noise_proc = processed.std()
    
    if noise_orig == 0:
        return 0
    
    reduction = ((noise_orig - noise_proc) / noise_orig) * 100
    return max(0, reduction)  # لا يمكن أن يكون سالباً

def show_lecture6():
    st.title("المحاضرة 6: كشف الحواف")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>كشف الحواف:</strong> تحديد النقاط التي تتغير فيها شدة الإضاءة بشكل حاد</p>
    <ul>
    <li><strong>التدرج (Gradient):</strong> معدل التغير في شدة البكسل</li>
    <li><strong>Sobel:</strong> كشف الحواف الأفقية والرأسية</li>
    <li><strong>Laplacian:</strong> كشف الحواف في جميع الاتجاهات</li>
    <li><strong>Canny:</strong> أفضل خوارزمية كشف حواف مع تحكم في العتبات</li>
    </ul>
    <p><strong>التطبيقات:</strong> تحليل الأشكال، كشف الكائنات، معالجة الصور الطبية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture6")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample6")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_edge_detection(image)
    elif use_sample:
        sample_image = create_detailed_sample_image()
        apply_edge_detection(sample_image)

def apply_edge_detection(image):
    """تطبيق تقنيات كشف الحواف"""
    st.markdown("### ⚙️ إعدادات كشف الحواف")
    
    # خيارات كشف الحواف
    col1, col2 = st.columns(2)
    
    with col1:
        edge_method = st.selectbox(
            "طريقة كشف الحواف:",
            ["Canny", "Sobel", "Laplacian", "Scharr", "Prewitt", "Roberts"]
        )
        
        # معالجة مسبقة
        apply_blur = st.checkbox("تطبيق تنعيم مسبق")
        if apply_blur:
            blur_kernel = st.slider("حجم فلتر التنعيم", 3, 15, 5, step=2)
    
    with col2:
        if edge_method == "Canny":
            threshold1 = st.slider("العتبة السفلى", 0, 255, 50)
            threshold2 = st.slider("العتبة العليا", 0, 255, 150)
            aperture_size = st.selectbox("حجم Aperture", [3, 5, 7])
        elif edge_method in ["Sobel", "Scharr"]:
            ksize = st.selectbox("حجم Kernel", [1, 3, 5, 7]) if edge_method == "Sobel" else 3
            show_direction = st.selectbox("اتجاه العرض:", ["Combined", "X Direction", "Y Direction", "Both Separate"])
        elif edge_method == "Laplacian":
            ksize = st.selectbox("حجم Kernel", [1, 3, 5, 7])
    
    # تحويل إلى رمادي
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image
    
    # تطبيق التنعيم المسبق إذا طُلب
    if apply_blur:
        working_image = cv2.GaussianBlur(gray_image, (blur_kernel, blur_kernel), 0)
    else:
        working_image = gray_image
    
    # تطبيق كشف الحواف
    if edge_method == "Canny":
        edges = cv2.Canny(working_image, threshold1, threshold2, apertureSize=aperture_size)
        
    elif edge_method == "Sobel":
        sobelx = cv2.Sobel(working_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(working_image, cv2.CV_64F, 0, 1, ksize=ksize)
        
        if show_direction == "Combined":
            edges = np.sqrt(sobelx**2 + sobely**2)
        elif show_direction == "X Direction":
            edges = np.abs(sobelx)
        elif show_direction == "Y Direction":
            edges = np.abs(sobely)
        
        edges = np.uint8(np.clip(edges, 0, 255))
        
    elif edge_method == "Scharr":
        scharrx = cv2.Scharr(working_image, cv2.CV_64F, 1, 0)
        scharry = cv2.Scharr(working_image, cv2.CV_64F, 0, 1)
        
        if show_direction == "Combined":
            edges = np.sqrt(scharrx**2 + scharry**2)
        elif show_direction == "X Direction":
            edges = np.abs(scharrx)
        elif show_direction == "Y Direction":
            edges = np.abs(scharry)
        
        edges = np.uint8(np.clip(edges, 0, 255))
        
    elif edge_method == "Laplacian":
        edges = cv2.Laplacian(working_image, cv2.CV_64F, ksize=ksize)
        edges = np.uint8(np.absolute(edges))
        
    elif edge_method == "Prewitt":
        # تطبيق مرشحات Prewitt
        kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
        kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
        
        prewittx = cv2.filter2D(working_image, cv2.CV_32F, kernelx)
        prewitty = cv2.filter2D(working_image, cv2.CV_32F, kernely)
        
        edges = np.sqrt(prewittx**2 + prewitty**2)
        edges = np.uint8(np.clip(edges, 0, 255))
        
    elif edge_method == "Roberts":
        # تطبيق مرشحات Roberts
        kernelx = np.array([[1, 0], [0, -1]], dtype=np.float32)
        kernely = np.array([[0, 1], [-1, 0]], dtype=np.float32)
        
        robertsx = cv2.filter2D(working_image, cv2.CV_32F, kernelx)
        robertsy = cv2.filter2D(working_image, cv2.CV_32F, kernely)
        
        edges = np.sqrt(robertsx**2 + robertsy**2)
        edges = np.uint8(np.clip(edges, 0, 255))
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    if edge_method in ["Sobel", "Scharr"] and show_direction == "Both Separate":
        # عرض الاتجاهات منفصلة
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("الصورة الأصلية")
            st.image(image, caption="Original", use_column_width=True)
        
        with col2:
            st.subheader("الاتجاه الأفقي (X)")
            if edge_method == "Sobel":
                edge_x = np.uint8(np.absolute(sobelx))
            else:
                edge_x = np.uint8(np.absolute(scharrx))
            st.image(edge_x, caption="X Direction", use_column_width=True, clamp=True)
        
        with col3:
            st.subheader("الاتجاه الرأسي (Y)")
            if edge_method == "Sobel":
                edge_y = np.uint8(np.absolute(sobely))
            else:
                edge_y = np.uint8(np.absolute(scharry))
            st.image(edge_y, caption="Y Direction", use_column_width=True, clamp=True)
        
        # عرض النتيجة المدمجة
        st.subheader("النتيجة المدمجة")
        combined_edges = np.sqrt((edge_x.astype(np.float32))**2 + (edge_y.astype(np.float32))**2)
        combined_edges = np.uint8(np.clip(combined_edges, 0, 255))
        st.image(combined_edges, caption="Combined Result", use_column_width=True, clamp=True)
        
    else:
        # عرض عادي
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("الصورة الأصلية")
            st.image(image, caption="Original Image", use_column_width=True)
            st.write(f"الأبعاد: {image.shape}")
        
        with col2:
            st.subheader(f"كشف الحواف - {edge_method}")
            st.image(edges, caption=f"Edges - {edge_method}", use_column_width=True, clamp=True)
            st.write(f"عدد نقاط الحواف: {np.count_nonzero(edges):,}")
    
    # إحصائيات الحواف
    st.markdown("### 📈 إحصائيات الحواف")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    
    with stats_col1:
        edge_pixels = np.count_nonzero(edges)
        total_pixels = edges.size
        edge_percentage = (edge_pixels / total_pixels) * 100
        st.metric("نسبة الحواف", f"{edge_percentage:.2f}%")
    
    with stats_col2:
        st.metric("شدة الحواف المتوسطة", f"{edges[edges > 0].mean():.1f}" if edge_pixels > 0 else "0")
    
    with stats_col3:
        st.metric("أقصى شدة حافة", f"{edges.max()}")
    
    # مقارنة بين الطرق المختلفة
    if st.checkbox("مقارنة بين طرق مختلفة"):
        st.markdown("### 🔍 مقارنة طرق كشف الحواف")
        
        methods = ["Canny", "Sobel", "Laplacian", "Scharr"]
        cols = st.columns(len(methods))
        
        for i, method in enumerate(methods):
            with cols[i]:
                if method == "Canny":
                    result = cv2.Canny(working_image, 50, 150)
                elif method == "Sobel":
                    sobelx = cv2.Sobel(working_image, cv2.CV_64F, 1, 0, ksize=3)
                    sobely = cv2.Sobel(working_image, cv2.CV_64F, 0, 1, ksize=3)
                    result = np.uint8(np.sqrt(sobelx**2 + sobely**2))
                elif method == "Laplacian":
                    result = np.uint8(np.absolute(cv2.Laplacian(working_image, cv2.CV_64F)))
                elif method == "Scharr":
                    scharrx = cv2.Scharr(working_image, cv2.CV_64F, 1, 0)
                    scharry = cv2.Scharr(working_image, cv2.CV_64F, 0, 1)
                    result = np.uint8(np.sqrt(scharrx**2 + scharry**2))
                
                st.subheader(method)
                st.image(result, caption=method, use_column_width=True, clamp=True)
                edge_count = np.count_nonzero(result)
                st.write(f"نقاط الحواف: {edge_count:,}")
    
    # معلومات تقنية
    st.markdown("### 📋 معلومات تقنية")
    
    info_text = f"""
    **الطريقة المستخدمة:** {edge_method}
    
    **المعاملات:**
    """
    
    if edge_method == "Canny":
        info_text += f"""
    - العتبة السفلى: {threshold1}
    - العتبة العليا: {threshold2}
    - حجم Aperture: {aperture_size}
    """
    elif edge_method in ["Sobel", "Laplacian"]:
        info_text += f"""
    - حجم Kernel: {ksize}
    """
    
    if apply_blur:
        info_text += f"""
    - تنعيم مسبق: نعم (حجم {blur_kernel})
    """
    else:
        info_text += """
    - تنعيم مسبق: لا
    """
    
    st.markdown(info_text)

def show_lecture7():
    st.title("المحاضرة 7: العمليات المورفولوجية")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>العمليات المورفولوجية:</strong> تطبق على الصور الثنائية لتحليل الأشكال</p>
    <ul>
    <li><strong>Erosion:</strong> تآكل - يقلل حجم الكائنات البيضاء</li>
    <li><strong>Dilation:</strong> توسع - يزيد حجم الكائنات البيضاء</li>
    <li><strong>Opening:</strong> فتح = Erosion ثم Dilation - يزيل الضوضاء الصغيرة</li>
    <li><strong>Closing:</strong> إغلاق = Dilation ثم Erosion - يملأ الثقوب الصغيرة</li>
    </ul>
    <p><strong>التطبيقات:</strong> تنظيف الصور الثنائية، فصل الكائنات، تحليل الأشكال</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture7")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample7")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_morphological_operations(image)
    elif use_sample:
        sample_image = create_binary_sample_image()
        apply_morphological_operations(sample_image)

def apply_morphological_operations(image):
    """تطبيق العمليات المورفولوجية"""
    st.markdown("### ⚙️ إعدادات العمليات المورفولوجية")
    
    # تحويل إلى صورة ثنائية
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image
    
    # خيارات التحويل إلى ثنائي
    col1, col2 = st.columns(2)
    
    with col1:
        threshold_method = st.selectbox("طريقة التحويل إلى ثنائي:", ["Manual", "Otsu", "Adaptive"])
        if threshold_method == "Manual":
            threshold_value = st.slider("قيمة العتبة", 0, 255, 127)
        elif threshold_method == "Adaptive":
            block_size = st.slider("حجم البلوك", 3, 21, 11, step=2)
            c_value = st.slider("قيمة C", -10, 10, 2)
    
    with col2:
        morph_operation = st.selectbox(
            "العملية المورفولوجية:",
            ["Erosion", "Dilation", "Opening", "Closing", "Gradient", "Top Hat", "Black Hat"]
        )
        
        kernel_shape = st.selectbox("شكل العنصر البنائي:", ["Rectangle", "Ellipse", "Cross"])
        kernel_size = st.slider("حجم العنصر البنائي", 3, 15, 5, step=2)
        iterations = st.slider("عدد التكرارات", 1, 5, 1)
    
    # تطبيق التحويل إلى ثنائي
    if threshold_method == "Manual":
        _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    elif threshold_method == "Otsu":
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    elif threshold_method == "Adaptive":
        binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c_value)
    
    # إنشاء العنصر البنائي
    if kernel_shape == "Rectangle":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif kernel_shape == "Ellipse":
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    elif kernel_shape == "Cross":
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    
    # تطبيق العملية المورفولوجية
    if morph_operation == "Erosion":
        result = cv2.erode(binary_image, kernel, iterations=iterations)
    elif morph_operation == "Dilation":
        result = cv2.dilate(binary_image, kernel, iterations=iterations)
    elif morph_operation == "Opening":
        result = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=iterations)
    elif morph_operation == "Closing":
        result = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    elif morph_operation == "Gradient":
        result = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel, iterations=iterations)
    elif morph_operation == "Top Hat":
        result = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel, iterations=iterations)
    elif morph_operation == "Black Hat":
        result = cv2.morphologyEx(binary_image, cv2.MORPH_BLACKHAT, kernel, iterations=iterations)
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("الصورة الأصلية")
        st.image(image, caption="Original", use_column_width=True)
    
    with col2:
        st.subheader("الصورة الثنائية")
        st.image(binary_image, caption=f"Binary - {threshold_method}", use_column_width=True, clamp=True)
    
    with col3:
        st.subheader(f"بعد {morph_operation}")
        st.image(result, caption=f"{morph_operation} Result", use_column_width=True, clamp=True)
    
    # إحصائيات
    st.markdown("### 📈 إحصائيات")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    
    with stats_col1:
        white_pixels_original = np.count_nonzero(binary_image)
        total_pixels = binary_image.size
        white_percentage_original = (white_pixels_original / total_pixels) * 100
        st.metric("البكسلات البيضاء الأصلية", f"{white_percentage_original:.1f}%")
    
    with stats_col2:
        white_pixels_result = np.count_nonzero(result)
        white_percentage_result = (white_pixels_result / total_pixels) * 100
        st.metric("البكسلات البيضاء بعد العملية", f"{white_percentage_result:.1f}%")
    
    with stats_col3:
        change = white_percentage_result - white_percentage_original
        st.metric("التغيير", f"{change:+.1f}%")
    
    # مقارنة العمليات المختلفة
    if st.checkbox("مقارنة العمليات المختلفة"):
        st.markdown("### 🔍 مقارنة العمليات المورفولوجية")
        
        operations = ["Erosion", "Dilation", "Opening", "Closing"]
        cols = st.columns(len(operations))
        
        for i, op in enumerate(operations):
            with cols[i]:
                if op == "Erosion":
                    op_result = cv2.erode(binary_image, kernel, iterations=1)
                elif op == "Dilation":
                    op_result = cv2.dilate(binary_image, kernel, iterations=1)
                elif op == "Opening":
                    op_result = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
                elif op == "Closing":
                    op_result = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
                
                st.subheader(op)
                st.image(op_result, caption=op, use_column_width=True, clamp=True)
                white_count = np.count_nonzero(op_result)
                st.write(f"بكسلات بيضاء: {white_count:,}")
    
    # عرض العنصر البنائي
    st.markdown("### 🔧 العنصر البنائي المستخدم")
    
    # تكبير العنصر البنائي للعرض
    display_kernel = cv2.resize(kernel.astype(np.uint8) * 255, (100, 100), interpolation=cv2.INTER_NEAREST)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(display_kernel, caption=f"{kernel_shape} Kernel ({kernel_size}x{kernel_size})", clamp=True)
    
    with col2:
        st.write("**معلومات العنصر البنائي:**")
        st.write(f"- الشكل: {kernel_shape}")
        st.write(f"- الحجم: {kernel_size}x{kernel_size}")
        st.write(f"- عدد التكرارات: {iterations}")
        st.write("**المصفوفة:**")
        st.write(kernel)
    
    # تأثيرات متتالية
    if st.checkbox("عرض تأثيرات متتالية"):
        st.markdown("### 🔄 تأثيرات متتالية")
        
        st.write("**Opening ثم Closing:**")
        opening_result = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
        opening_closing_result = cv2.morphologyEx(opening_result, cv2.MORPH_CLOSE, kernel)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(binary_image, caption="Original Binary", use_column_width=True, clamp=True)
        with col2:
            st.image(opening_result, caption="After Opening", use_column_width=True, clamp=True)
        with col3:
            st.image(opening_closing_result, caption="After Opening + Closing", use_column_width=True, clamp=True)
        
        st.write("**Closing ثم Opening:**")
        closing_result = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
        closing_opening_result = cv2.morphologyEx(closing_result, cv2.MORPH_OPEN, kernel)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(binary_image, caption="Original Binary", use_column_width=True, clamp=True)
        with col2:
            st.image(closing_result, caption="After Closing", use_column_width=True, clamp=True)
        with col3:
            st.image(closing_opening_result, caption="After Closing + Opening", use_column_width=True, clamp=True)

def create_binary_sample_image():
    """إنشاء صورة نموذجية للعمليات المورفولوجية"""
    height, width = 200, 300
    image = np.zeros((height, width), dtype=np.uint8)
    
    # إضافة أشكال مختلفة
    # مربعات
    cv2.rectangle(image, (50, 50), (100, 100), 255, -1)
    cv2.rectangle(image, (150, 50), (200, 100), 255, -1)
    
    # دوائر
    cv2.circle(image, (75, 150), 25, 255, -1)
    cv2.circle(image, (175, 150), 20, 255, -1)
    
    # خطوط رفيعة
    cv2.line(image, (20, 20), (280, 20), 255, 2)
    cv2.line(image, (20, 180), (280, 180), 255, 1)
    
    # إضافة ضوضاء صغيرة
    for _ in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        cv2.circle(image, (x, y), 2, 255, -1)
    
    # إضافة ثقوب صغيرة في الأشكال
    cv2.circle(image, (75, 75), 5, 0, -1)
    cv2.circle(image, (175, 75), 3, 0, -1)
    
    return image

def show_lecture8():
    st.title("المحاضرة 8: التحويلات الهندسية")
    
    # الجزء النظري
    st.markdown("""
    <div class="theory-box">
    <h3>🎓 الجزء النظري</h3>
    <p><strong>التحويلات الهندسية:</strong> تغيير موضع أو حجم أو اتجاه الصورة</p>
    <ul>
    <li><strong>Translation:</strong> إزاحة - نقل الصورة في الاتجاهات X و Y</li>
    <li><strong>Rotation:</strong> دوران - تدوير الصورة حول نقطة معينة</li>
    <li><strong>Scaling:</strong> تكبير/تصغير - تغيير حجم الصورة</li>
    <li><strong>Flipping:</strong> انعكاس - قلب الصورة أفقياً أو رأسياً</li>
    </ul>
    <p><strong>التطبيقات:</strong> تصحيح الصور، تحسين العرض، معالجة البيانات</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # الجزء العملي
    st.markdown("## 🔬 الجزء العملي")
    
    # تحميل الصورة
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة", type=['png', 'jpg', 'jpeg'], key="lecture8")
    
    with col2:
        use_sample = st.button("استخدم صورة نموذجية", key="sample8")
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        apply_geometric_transforms(image)
    elif use_sample:
        sample_image = create_sample_image()
        apply_geometric_transforms(sample_image)

def apply_geometric_transforms(image):
    """تطبيق التحويلات الهندسية"""
    st.markdown("### ⚙️ إعدادات التحويلات الهندسية")
    
    # خيارات التحويل
    transform_type = st.selectbox(
        "نوع التحويل:",
        ["Translation", "Rotation", "Scaling", "Flipping", "Cropping", "Affine Transform"]
    )
    
    height, width = image.shape[:2]
    
    # معاملات التحويل حسب النوع
    if transform_type == "Translation":
        col1, col2 = st.columns(2)
        with col1:
            tx = st.slider("الإزاحة الأفقية (X)", -width//2, width//2, 0)
        with col2:
            ty = st.slider("الإزاحة الرأسية (Y)", -height//2, height//2, 0)
        
        # مصفوفة التحويل
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        transformed = cv2.warpAffine(image, M, (width, height))
        
    elif transform_type == "Rotation":
        col1, col2, col3 = st.columns(3)
        with col1:
            angle = st.slider("زاوية الدوران (درجة)", -180, 180, 0)
        with col2:
            scale = st.slider("معامل التكبير", 0.1, 2.0, 1.0, 0.1)
        with col3:
            center_x = st.slider("مركز الدوران X", 0, width, width//2)
            center_y = st.slider("مركز الدوران Y", 0, height, height//2)
        
        # مصفوفة التحويل
        center = (center_x, center_y)
        M = cv2.getRotationMatrix2D(center, angle, scale)
        transformed = cv2.warpAffine(image, M, (width, height))
        
    elif transform_type == "Scaling":
        col1, col2 = st.columns(2)
        with col1:
            scale_x = st.slider("معامل التكبير الأفقي", 0.1, 3.0, 1.0, 0.1)
        with col2:
            scale_y = st.slider("معامل التكبير الرأسي", 0.1, 3.0, 1.0, 0.1)
        
        new_width = int(width * scale_x)
        new_height = int(height * scale_y)
        transformed = cv2.resize(image, (new_width, new_height))
        
    elif transform_type == "Flipping":
        flip_direction = st.selectbox("اتجاه الانعكاس:", ["أفقي", "رأسي", "كلاهما"])
        
        if flip_direction == "أفقي":
            transformed = cv2.flip(image, 1)
        elif flip_direction == "رأسي":
            transformed = cv2.flip(image, 0)
        elif flip_direction == "كلاهما":
            transformed = cv2.flip(image, -1)
            
    elif transform_type == "Cropping":
        col1, col2 = st.columns(2)
        with col1:
            x1 = st.slider("X البداية", 0, width-1, 0)
            y1 = st.slider("Y البداية", 0, height-1, 0)
        with col2:
            x2 = st.slider("X النهاية", x1+1, width, width)
            y2 = st.slider("Y النهاية", y1+1, height, height)
        
        transformed = image[y1:y2, x1:x2]
        
    elif transform_type == "Affine Transform":
        st.write("**تحديد النقاط للتحويل الأفيني:**")
        
        # نقاط المصدر (افتراضية)
        src_points = np.float32([[0, 0], [width-1, 0], [0, height-1]])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("النقطة 1:")
            dst_x1 = st.slider("X1", 0, width-1, 0, key="dst_x1")
            dst_y1 = st.slider("Y1", 0, height-1, 0, key="dst_y1")
        
        with col2:
            st.write("النقطة 2:")
            dst_x2 = st.slider("X2", 0, width-1, width-1, key="dst_x2")
            dst_y2 = st.slider("Y2", 0, height-1, 0, key="dst_y2")
        
        with col3:
            st.write("النقطة 3:")
            dst_x3 = st.slider("X3", 0, width-1, 0, key="dst_x3")
            dst_y3 = st.slider("Y3", 0, height-1, height-1, key="dst_y3")
        
        dst_points = np.float32([[dst_x1, dst_y1], [dst_x2, dst_y2], [dst_x3, dst_y3]])
        
        # مصفوفة التحويل الأفيني
        M = cv2.getAffineTransform(src_points, dst_points)
        transformed = cv2.warpAffine(image, M, (width, height))
    
    # عرض النتائج
    st.markdown("### 📊 النتائج")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("الصورة الأصلية")
        st.image(image, caption="Original Image", use_column_width=True)
        st.write(f"الأبعاد: {image.shape}")
    
    with col2:
        st.subheader(f"بعد {transform_type}")
        st.image(transformed, caption=f"Transformed - {transform_type}", use_column_width=True)
        st.write(f"الأبعاد: {transformed.shape}")
    
    # معلومات التحويل
    st.markdown("### 📋 معلومات التحويل")
    
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.write(f"**نوع التحويل:** {transform_type}")
        
        if transform_type == "Translation":
            st.write(f"**الإزاحة:** ({tx}, {ty})")
        elif transform_type == "Rotation":
            st.write(f"**الزاوية:** {angle}°")
            st.write(f"**المركز:** ({center_x}, {center_y})")
            st.write(f"**معامل التكبير:** {scale}")
        elif transform_type == "Scaling":
            st.write(f"**معامل التكبير:** ({scale_x}, {scale_y})")
        elif transform_type == "Flipping":
            st.write(f"**الاتجاه:** {flip_direction}")
        elif transform_type == "Cropping":
            st.write(f"**المنطقة:** ({x1}, {y1}) إلى ({x2}, {y2})")
    
    with info_col2:
        # حساب التغيير في الحجم
        original_size = image.shape[0] * image.shape[1]
        transformed_size = transformed.shape[0] * transformed.shape[1]
        size_change = ((transformed_size - original_size) / original_size) * 100
        
        st.write(f"**الحجم الأصلي:** {original_size:,} بكسل")
        st.write(f"**الحجم الجديد:** {transformed_size:,} بكسل")
        st.write(f"**التغيير:** {size_change:+.1f}%")
    
    # مقارنة متعددة
    if st.checkbox("مقارنة تحويلات متعددة"):
        st.markdown("### 🔍 مقارنة التحويلات المختلفة")
        
        transforms = {
            "الأصلية": image,
            "دوران 45°": cv2.warpAffine(image, cv2.getRotationMatrix2D((width//2, height//2), 45, 1), (width, height)),
            "انعكاس أفقي": cv2.flip(image, 1),
            "تكبير 1.5x": cv2.resize(image, (int(width*1.5), int(height*1.5)))
        }
        
        cols = st.columns(len(transforms))
        
        for i, (name, img) in enumerate(transforms.items()):
            with cols[i]:
                st.subheader(name)
                st.image(img, caption=name, use_column_width=True)
                st.write(f"الأبعاد: {img.shape[:2]}")
    
    # تحويلات متتالية
    if st.checkbox("تطبيق تحويلات متتالية"):
        st.markdown("### 🔄 تحويلات متتالية")
        
        # تطبيق سلسلة من التحويلات
        step1 = cv2.flip(image, 1)  # انعكاس أفقي
        step2 = cv2.warpAffine(step1, cv2.getRotationMatrix2D((width//2, height//2), 30, 1), (width, height))  # دوران
        step3 = cv2.resize(step2, (int(width*0.8), int(height*0.8)))  # تصغير
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.subheader("الأصلية")
            st.image(image, caption="Original", use_column_width=True)
        
        with col2:
            st.subheader("انعكاس")
            st.image(step1, caption="Flipped", use_column_width=True)
        
        with col3:
            st.subheader("دوران")
            st.image(step2, caption="Rotated", use_column_width=True)
        
        with col4:
            st.subheader("تصغير")
            st.image(step3, caption="Scaled", use_column_width=True)
    
    # عرض مصفوفة التحويل
    if transform_type in ["Translation", "Rotation", "Affine Transform"]:
        st.markdown("### 🔢 مصفوفة التحويل")
        
        if transform_type == "Translation":
            matrix_display = M
        elif transform_type == "Rotation":
            matrix_display = M
        elif transform_type == "Affine Transform":
            matrix_display = M
        
        st.write("**مصفوفة التحويل المستخدمة:**")
        st.write(matrix_display)
        
        # شرح المصفوفة
        if transform_type == "Translation":
            st.write("""
            **شرح المصفوفة:**
            - العمود الأول: معامل X (1 = بدون تغيير)
            - العمود الثاني: معامل Y (1 = بدون تغيير)  
            - العمود الثالث: الإزاحة (tx, ty)
            """)
        elif transform_type == "Rotation":
            st.write("""
            **شرح المصفوفة:**
            - cos(θ), -sin(θ): معاملات الدوران
            - sin(θ), cos(θ): معاملات الدوران
            - العمود الثالث: الإزاحة بعد الدوران
            """)

def show_lecture9():
    st.title("المحاضرة 9: المشروع الختامي")
    
    # مقدمة المشروع
    st.markdown("""
    <div class="theory-box">
    <h3>🎯 المشروع الختامي</h3>
    <p><strong>الهدف:</strong> تطبيق شامل لجميع تقنيات معالجة الصور التي تعلمناها</p>
    <p>في هذا المشروع، ستتمكن من:</p>
    <ul>
    <li>رفع صورة أو استخدام صورة نموذجية</li>
    <li>بناء pipeline معالجة مخصص</li>
    <li>تطبيق عمليات متتالية</li>
    <li>مقارنة النتائج وحفظها</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # تحميل الصورة
    st.markdown("## 📁 تحميل الصورة")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("اختر صورة للمعالجة", type=['png', 'jpg', 'jpeg'], key="final_project")
    
    with col2:
        sample_options = st.selectbox(
            "أو اختر صورة نموذجية:",
            ["لا شيء", "صورة ملونة بسيطة", "صورة مفصلة", "صورة ثنائية", "صورة بضوضاء"]
        )
        
        if sample_options != "لا شيء":
            if sample_options == "صورة ملونة بسيطة":
                image = create_sample_image()
            elif sample_options == "صورة مفصلة":
                image = create_detailed_sample_image()
            elif sample_options == "صورة ثنائية":
                image = create_binary_sample_image()
            elif sample_options == "صورة بضوضاء":
                base_image = create_sample_image()
                image = add_noise_to_image(base_image, "Gaussian", 0.1)
        elif uploaded_file is not None:
            image = load_image(uploaded_file)
        else:
            image = None
    
    if image is not None:
        # عرض الصورة الأصلية
        st.markdown("### 🖼️ الصورة الأصلية")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(image, caption="الصورة الأصلية", use_column_width=True)
        
        with col2:
            st.write(f"**الأبعاد:** {image.shape}")
            st.write(f"**النوع:** {'ملونة' if len(image.shape) == 3 else 'رمادية'}")
            st.write(f"**الحجم:** {image.size:,} بكسل")
            st.write(f"**متوسط القيم:** {image.mean():.1f}")
        
        st.markdown("---")
        
        # بناء Pipeline المعالجة
        st.markdown("## ⚙️ بناء Pipeline المعالجة")
        
        # اختيار العمليات
        st.markdown("### 1️⃣ اختيار العمليات")
        
        operations = []
        
        # العملية الأولى
        op1 = st.selectbox("العملية الأولى:", 
                          ["لا شيء", "تحويل إلى رمادي", "تعديل السطوع/التباين", "تطبيق فلتر", "كشف الحواف"])
        
        if op1 != "لا شيء":
            operations.append(op1)
            
            if op1 == "تعديل السطوع/التباين":
                col1, col2 = st.columns(2)
                with col1:
                    brightness1 = st.slider("السطوع", -100, 100, 0, key="bright1")
                with col2:
                    contrast1 = st.slider("التباين", 0.1, 3.0, 1.0, 0.1, key="contrast1")
            
            elif op1 == "تطبيق فلتر":
                filter1 = st.selectbox("نوع الفلتر:", ["Blur", "Gaussian Blur", "Sharpen"], key="filter1")
                if filter1 in ["Blur", "Gaussian Blur"]:
                    kernel_size1 = st.slider("حجم الفلتر", 3, 15, 5, step=2, key="kernel1")
            
            elif op1 == "كشف الحواف":
                edge_method1 = st.selectbox("طريقة كشف الحواف:", ["Canny", "Sobel", "Laplacian"], key="edge1")
                if edge_method1 == "Canny":
                    threshold1_1 = st.slider("العتبة السفلى", 0, 255, 50, key="thresh1_1")
                    threshold2_1 = st.slider("العتبة العليا", 0, 255, 150, key="thresh2_1")
        
        # العملية الثانية
        if operations:
            op2 = st.selectbox("العملية الثانية:", 
                              ["لا شيء", "تطبيق فلتر", "عمليات مورفولوجية", "تحويل هندسي", "إزالة الضوضاء"])
            
            if op2 != "لا شيء":
                operations.append(op2)
                
                if op2 == "تطبيق فلتر":
                    filter2 = st.selectbox("نوع الفلتر:", ["Median", "Bilateral", "Emboss"], key="filter2")
                    if filter2 == "Median":
                        kernel_size2 = st.slider("حجم الفلتر", 3, 15, 5, step=2, key="kernel2")
                
                elif op2 == "عمليات مورفولوجية":
                    morph_op2 = st.selectbox("العملية المورفولوجية:", ["Opening", "Closing", "Erosion", "Dilation"], key="morph2")
                    morph_kernel_size2 = st.slider("حجم العنصر البنائي", 3, 15, 5, step=2, key="morph_kernel2")
                
                elif op2 == "تحويل هندسي":
                    transform2 = st.selectbox("نوع التحويل:", ["Rotation", "Scaling", "Flipping"], key="transform2")
                    if transform2 == "Rotation":
                        angle2 = st.slider("زاوية الدوران", -180, 180, 0, key="angle2")
                    elif transform2 == "Scaling":
                        scale2 = st.slider("معامل التكبير", 0.1, 2.0, 1.0, 0.1, key="scale2")
                    elif transform2 == "Flipping":
                        flip_dir2 = st.selectbox("اتجاه الانعكاس:", ["أفقي", "رأسي"], key="flip2")
        
        # العملية الثالثة
        if len(operations) >= 2:
            op3 = st.selectbox("العملية الثالثة:", 
                              ["لا شيء", "تحسين الصورة", "كشف الحواف النهائي", "تطبيق عتبة"])
            
            if op3 != "لا شيء":
                operations.append(op3)
                
                if op3 == "تحسين الصورة":
                    enhance_type = st.selectbox("نوع التحسين:", ["Sharpen", "Contrast Enhancement"], key="enhance3")
                elif op3 == "كشف الحواف النهائي":
                    final_edge = st.selectbox("طريقة كشف الحواف:", ["Canny", "Sobel"], key="final_edge")
                elif op3 == "تطبيق عتبة":
                    threshold_method = st.selectbox("طريقة العتبة:", ["Manual", "Otsu"], key="thresh_method")
                    if threshold_method == "Manual":
                        threshold_val = st.slider("قيمة العتبة", 0, 255, 127, key="thresh_val")
        
        # تطبيق Pipeline
        if st.button("🚀 تطبيق Pipeline", type="primary"):
            st.markdown("### 📊 نتائج المعالجة")
            
            # تطبيق العمليات تدريجياً
            current_image = image.copy()
            results = [("الصورة الأصلية", current_image)]
            
            for i, operation in enumerate(operations):
                if operation == "تحويل إلى رمادي":
                    if len(current_image.shape) == 3:
                        current_image = cv2.cvtColor(current_image, cv2.COLOR_RGB2GRAY)
                    results.append(("رمادي", current_image))
                
                elif operation == "تعديل السطوع/التباين":
                    processed = current_image.copy().astype(np.float32)
                    processed = contrast1 * processed + brightness1
                    current_image = np.clip(processed, 0, 255).astype(np.uint8)
                    results.append((f"سطوع/تباين", current_image))
                
                elif operation == "تطبيق فلتر":
                    if i == 0:  # العملية الأولى
                        if filter1 == "Blur":
                            current_image = cv2.blur(current_image, (kernel_size1, kernel_size1))
                        elif filter1 == "Gaussian Blur":
                            current_image = cv2.GaussianBlur(current_image, (kernel_size1, kernel_size1), 0)
                        elif filter1 == "Sharpen":
                            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
                            current_image = cv2.filter2D(current_image, -1, kernel)
                        results.append((f"فلتر {filter1}", current_image))
                    else:  # العملية الثانية
                        if filter2 == "Median":
                            current_image = cv2.medianBlur(current_image, kernel_size2)
                        elif filter2 == "Bilateral":
                            current_image = cv2.bilateralFilter(current_image, 9, 75, 75)
                        elif filter2 == "Emboss":
                            kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
                            current_image = cv2.filter2D(current_image, -1, kernel)
                        results.append((f"فلتر {filter2}", current_image))
                
                elif operation == "كشف الحواف":
                    if len(current_image.shape) == 3:
                        gray = cv2.cvtColor(current_image, cv2.COLOR_RGB2GRAY)
                    else:
                        gray = current_image
                    
                    if edge_method1 == "Canny":
                        current_image = cv2.Canny(gray, threshold1_1, threshold2_1)
                    elif edge_method1 == "Sobel":
                        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
                        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
                        current_image = np.uint8(np.sqrt(sobelx**2 + sobely**2))
                    elif edge_method1 == "Laplacian":
                        current_image = np.uint8(np.absolute(cv2.Laplacian(gray, cv2.CV_64F)))
                    
                    results.append((f"حواف {edge_method1}", current_image))
                
                elif operation == "عمليات مورفولوجية":
                    if len(current_image.shape) == 3:
                        gray = cv2.cvtColor(current_image, cv2.COLOR_RGB2GRAY)
                    else:
                        gray = current_image
                    
                    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (morph_kernel_size2, morph_kernel_size2))
                    
                    if morph_op2 == "Opening":
                        current_image = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
                    elif morph_op2 == "Closing":
                        current_image = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
                    elif morph_op2 == "Erosion":
                        current_image = cv2.erode(binary, kernel)
                    elif morph_op2 == "Dilation":
                        current_image = cv2.dilate(binary, kernel)
                    
                    results.append((f"مورفولوجي {morph_op2}", current_image))
                
                elif operation == "تحويل هندسي":
                    height, width = current_image.shape[:2]
                    
                    if transform2 == "Rotation":
                        M = cv2.getRotationMatrix2D((width//2, height//2), angle2, 1)
                        current_image = cv2.warpAffine(current_image, M, (width, height))
                    elif transform2 == "Scaling":
                        new_width = int(width * scale2)
                        new_height = int(height * scale2)
                        current_image = cv2.resize(current_image, (new_width, new_height))
                    elif transform2 == "Flipping":
                        if flip_dir2 == "أفقي":
                            current_image = cv2.flip(current_image, 1)
                        elif flip_dir2 == "رأسي":
                            current_image = cv2.flip(current_image, 0)
                    
                    results.append((f"تحويل {transform2}", current_image))
            
            # عرض النتائج
            cols_per_row = 3
            for i in range(0, len(results), cols_per_row):
                cols = st.columns(cols_per_row)
                for j in range(cols_per_row):
                    if i + j < len(results):
                        with cols[j]:
                            name, img = results[i + j]
                            st.subheader(name)
                            st.image(img, caption=name, use_column_width=True, clamp=True)
                            if hasattr(img, 'shape'):
                                st.write(f"الأبعاد: {img.shape}")
            
            # إحصائيات المقارنة
            st.markdown("### 📈 إحصائيات المقارنة")
            
            final_image = results[-1][1]
            
            stats_col1, stats_col2, stats_col3 = st.columns(3)
            
            with stats_col1:
                st.metric("عدد العمليات المطبقة", len(operations))
                st.metric("الأبعاد الأصلية", f"{image.shape[0]}×{image.shape[1]}")
            
            with stats_col2:
                st.metric("الأبعاد النهائية", f"{final_image.shape[0]}×{final_image.shape[1]}")
                original_size = image.shape[0] * image.shape[1]
                final_size = final_image.shape[0] * final_image.shape[1]
                size_change = ((final_size - original_size) / original_size) * 100
                st.metric("تغيير الحجم", f"{size_change:+.1f}%")
            
            with stats_col3:
                st.metric("متوسط القيم الأصلية", f"{image.mean():.1f}")
                st.metric("متوسط القيم النهائية", f"{final_image.mean():.1f}")
            
            # خيار حفظ النتيجة
            st.markdown("### 💾 حفظ النتيجة")
            
            if st.button("حفظ الصورة النهائية"):
                # تحويل إلى PIL للحفظ
                if len(final_image.shape) == 3:
                    pil_image = Image.fromarray(final_image)
                else:
                    pil_image = Image.fromarray(final_image)
                
                # حفظ الصورة
                output_path = "/home/ubuntu/image_processing_app/processed_image.png"
                pil_image.save(output_path)
                
                st.success(f"تم حفظ الصورة في: {output_path}")
                
                # عرض رابط التحميل
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="تحميل الصورة المعالجة",
                        data=file.read(),
                        file_name="processed_image.png",
                        mime="image/png"
                    )
    
    else:
        st.info("يرجى تحميل صورة أو اختيار صورة نموذجية لبدء المشروع.")
    
    # خلاصة السلسلة
    st.markdown("---")
    st.markdown("""
    ## 🎓 خلاصة السلسلة
    
    تهانينا! لقد أكملت سلسلة محاضرات معالجة الصور التفاعلية. 
    
    **ما تعلمته:**
    - أساسيات الصور الرقمية ومعمارية البكسل
    - أنظمة الألوان وتحويلاتها
    - العمليات النقطية والتحكم في السطوع والتباين
    - الفلاتر والالتفاف لتحسين جودة الصور
    - تقنيات إزالة الضوضاء المتقدمة
    - خوارزميات كشف الحواف
    - العمليات المورفولوجية لتحليل الأشكال
    - التحويلات الهندسية
    - بناء pipeline معالجة شامل
    
    **الخطوات التالية:**
    - جرب تطبيق هذه التقنيات على صورك الخاصة
    - اكتشف تطبيقات أخرى في الرؤية الحاسوبية
    - تعلم المزيد عن التعلم العميق في معالجة الصور
    """)
    
    st.balloons()  # احتفال بإنهاء السلسلة!

# دوال مساعدة لمعالجة الصور
def load_image(image_file):
    """تحميل الصورة من الملف المرفوع"""
    img = Image.open(image_file)
    return np.array(img)

def convert_to_opencv(pil_image):
    """تحويل صورة PIL إلى تنسيق OpenCV"""
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def convert_to_pil(opencv_image):
    """تحويل صورة OpenCV إلى تنسيق PIL"""
    return Image.fromarray(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB))

if __name__ == "__main__":
    main()

