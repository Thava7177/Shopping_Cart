�
    ���fQ  �                   ��   � d dl mZ ddl�  G d� dej                  �      Z G d� dej                  �      Zej                  j                  ee�       ej                  j                  e	e�       y)	�    )�admin�   )�*c                   �   � e Zd ZdZy)�CategoryAdmin)�name�image�descriptionN��__name__�
__module__�__qualname__�list_display� �    �7C:\Users\thava\OneDrive\Desktop\Shop_Kart\App1\admin.pyr   r      s   � �/�Lr   r   c                   �   � e Zd ZdZy)�ProductAdmin)r   �product_imager
   Nr   r   r   r   r   r      s   � �7�Lr   r   N)
�django.contribr   �models�
ModelAdminr   r   �site�register�Catagory�Productr   r   r   �<module>r      sY   ��  � �0�E�$�$� 0�8�E�$�$� 8� �
�
� � �H�]� +� �
�
� � �G�L� )r   