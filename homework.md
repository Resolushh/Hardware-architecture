# Практическая работа по BIOS и UEFI

Работал в графическом режиме симулятора Lenovo. Основная модель ThinkPad X1 Carbon 12th Gen.

[Lenovo BIOS Simulator Center](https://download.lenovo.com/bsco/index.html)

## 1. Основные разделы

Открыл Main, Config, Security, Startup и Restart. В Main нашел версию UEFI N3YET50W, серийный номер PF12345 и процессор Intel Core.

![Основные разделы](screenshots/01-main.jpg)

![Основные разделы](screenshots/02-config.jpg)

![Основные разделы](screenshots/03-security.jpg)

![Основные разделы](screenshots/04-startup.jpg)

![Основные разделы](screenshots/05-restart.jpg)

## 2. Порядок загрузки

На T14s Gen 5 открыл Boot в разделе Startup. Перетащил строки за свободный край справа. USB HDD поставил первым, NVMe вторым.

![USB HDD первым, NVMe вторым](screenshots/39-usb-nvme.jpg)

## 3. Secure Boot

В Security открыл Secure Boot, выключил его и включил обратно. Статус менялся сразу, без перезагрузки симулятора. Secure Boot проверяет подпись загрузчика.

![Secure Boot выключен](screenshots/12-secure-off.jpg)

![Secure Boot включен](screenshots/13-secure-on.jpg)

## 4. Пароль супервизора

На T14s Gen 5 установил Supervisor Password в разделе Security, в меню Password. На X1 Carbon при изменении настройки запроса пароля не было. Снять пароль получилось через Load Factory Defaults в разделе Restart.

![Пароль установлен](screenshots/33-t14s-enabled.jpg)

![Подтверждение заводского сброса](screenshots/37-t14s-reset-confirm.jpg)

![Пароль снят после сброса](screenshots/38-t14s-password-after-reset.jpg)

## 5. Заводские настройки

В Restart выбрал Load Factory Defaults и подтвердил сброс. Для сброса также есть F9. Порядок загрузки остался прежним, Secure Boot был включен, а пароль сброс не снял.

![Заводские настройки](screenshots/14-defaults.jpg)

На ThinkPad E14 Gen 5 AMD выключил Always On USB. После Load Setup Defaults настройка вернулась в On.

![USB до сброса](screenshots/27-before-defaults.jpg)

![USB после сброса](screenshots/28-after-defaults.jpg)

## 6. Питание USB

В разделе Config открыл USB. Выключил Always On USB и включил обратно.

![Always On USB выключен](screenshots/10-usb-off.jpg)

![Always On USB включен](screenshots/11-usb-on.jpg)

## 7. Режим SATA или NVMe

На ThinkPad P16 Gen 2 в разделе Config открыл Storage и включил VMD Controller. Появилось меню Intel RST. Затем выключил VMD. Предупреждения не было.

![VMD включен, меню Intel RST доступно](screenshots/24-vmd-on.jpg)

![VMD возвращен в исходное состояние](screenshots/25-vmd-off.jpg)

## 8. Временное меню F12

В Startup выключил Boot device List F12 Option и включил обратно. F12 позволяет выбрать устройство на один запуск.

![Временное меню F12](screenshots/15-f12.jpg)

## 9. Журнал событий

На T14s Gen 5 открыл Main. Журнал BIOS Event log недоступен, поэтому просмотреть и очистить записи не получилось.

![Журнал событий](screenshots/32-t14s-log.jpg)

## 10. Подготовка к переустановке ОС

На T14s Gen 5 подтвердил сохранение через F10. Симулятор остался в Setup. Снова открыл Boot и проверил, что USB HDD стоит первым, а NVMe вторым.

![Подтверждение сохранения](screenshots/40-usb-save.jpg)

![Порядок после повторного открытия Boot](screenshots/41-usb-reopen.jpg)
