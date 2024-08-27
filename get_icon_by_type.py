from markupsafe import Markup

class GetIconByType():
    
    def get_icon_by_type(self, type):
        match type:
            case 'text/csv':
                return Markup('<i class="fa-solid fa-file-csv fa-2x"></i>')
            case 'application/pdf':
                return Markup('<i class="fa-solid fa-file-pdf fa-2x"></i>')
            case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                return Markup('<i class="fa-solid fa-file-excel fa-2x"></i>')
            case 'image/png':
                return Markup('<i class="fa-solid fa-file-image fa-2x"></i>')
            case 'image/jpeg':
                return Markup('<i class="fa-solid fa-file-image fa-2x"></i>')
            case 'video/quicktime':
                return Markup('<i class="fa-solid fa-file-video fa-2x"></i>')
            case 'text/html':
                return Markup('<i class="fa-brands fa-html5 fa-2x"></i>')
            case 'inode/x-empty':
                return Markup('<i class="fa-brands fa-js fa-2x"></i>')
            case 'audio/mpeg':
                return Markup('<i class="fa-regular fa-file-audio fa-2x"></i>')
            case _:
                return Markup('<i class="fa-solid fa-file fa-2x"></i>')