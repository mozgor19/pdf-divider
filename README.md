# PDF Divider

PDF Divider, kullanıcıların PDF dosyalarını belirli sayfa aralıklarına göre bölmelerine olanak tanıyan bir PyQt5 masaüstü uygulamasıdır.

## Kullanım

Uygulamayı başlatmak için `main.py` dosyasını çalıştırın. Uygulama başladığında, aşağıdaki özelliklere sahip bir arayüz göreceksiniz:

- **PDF Seç:** Bölmek istediğiniz PDF dosyasını seçmek için bu düğmeye tıklayın.
- **Aralıkları Girin:** PDF dosyasının hangi sayfa aralıklarını bölmek istediğinizi belirtin. Örneğin, "120-130, 145-180" gibi.
- **Çıktıyı Kaydet:** Böldüğünüz sayfaları kaydetmek için bu düğmeye tıklayın. Kaydetmek istediğiniz dosyanın adını ve konumunu seçin.
- **Başarılı bir şekilde kaydedildi:** Sayfalar başarıyla kaydedildiğinde bu mesaj görüntülenir.
- **Dosya Konumuna Git:** Kaydedilen dosyanın bulunduğu klasöre gitmek için bu düğmeye tıklayın.

## Kurulum

1. Bu repo'yu klonlayın:

```bash
git clone https://github.com/mozgor19/pdf-tools.git
```

2. Gerekli Python kütüphanelerini yükleyin:

```bash
pip install -r requirements.txt
```
3. Uygulamayı başlatın:

```bash
python main.py
```

# PyQt5 Uygulamasını Dağıtma Rehberi

Bu rehber, PyQt5 ile geliştirilmiş bir uygulamayı kullanıcılara dağıtmak için adım adım talimatlar içerir.

## Adım 1: PyInstaller Kurulumu

PyInstaller'ı yüklemek için terminal veya komut istemcisine şu komutu yazın:

```bash
pip install pyinstaller
```
## Adım 2: Uygulamanın Hazırlanması
PyQt5 uygulamanızın ana dosyasını (main.py gibi) ve diğer gerekli dosyaları içeren bir klasör oluşturun. Örneğin:

```bash
myapp/
├── main.py
├── logo.ico
├── pdf_divider.py
```
## Adım 3: Uygulamanın Paketlenmesi

Terminalde veya komut istemcisinde uygulamanın bulunduğu dizine gidin ve şu komutu çalıştırın:

```bash
pyinstaller main.py
```
Bu komut, PyQt5 uygulamanızı platforma özgü bir yürütülebilir dosyaya dönüştürecektir. Bu işlem tamamlandığında, "dist" adlı yeni bir klasör oluşturulur ve bu klasörde dönüştürülmüş uygulama bulunur.

## Adım 4: Dağıtım Dosyalarını Paketleme

Dönüştürülmüş uygulamayı kullanıcıya dağıtmak için, "dist" klasöründeki ilgili dosyaları paketlemeniz gerekebilir. Örneğin, Windows için bir yürütülebilir dosya (.exe) oluşturulduysa, bu dosyayı bir zip dosyası içine koyabilirsiniz.

## Adım 5: Kullanıcıya Dağıtım

Zip dosyasını kullanıcılarla paylaşın. Kullanıcılar bu dosyayı indirip kendi bilgisayarlarında çıkartarak uygulamayı çalıştırabilirler. Kullanıcılara uygulamayı çalıştırabilmeleri için Python veya PyQt5 yüklemelerine gerek kalmayacaktır, çünkü PyInstaller, tüm gerekli kütüphaneleri yürütülebilir dosyanın içine dahil eder.

